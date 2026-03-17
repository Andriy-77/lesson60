from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from .forms import OrderForm
from django.core.mail import send_mail
from .models import Order, PricingPackage, PageView, OrderAnalytics
from django.conf import settings
from django.core import validators
from django.core.exceptions import ValidationError
from django.db.models import Count
from django.db.models.functions import TruncMonth
from datetime import datetime, timedelta

def pricing_view(request):
    packages = PricingPackage.objects.all()
    return render(request, "orders/pricing.html", {"packages": packages})

def analytics_view(request):
    total_orders = Order.objects.count()
    done_orders = Order.objects.filter(status="done").count()
    months_qs = (
        Order.objects.annotate(month=TruncMonth("created_at"))
        .values("month")
        .annotate(count=Count("id"))
        .order_by("month")
    )

    months = [
        {"month": m["month"].strftime("%Y-%m") if m["month"] else "—", "count": m["count"]}
        for m in months_qs
    ]

    top_pages = PageView.objects.order_by("-views")[:10]

    # Popular projects by internal view counter
    from portfolio.models import Project

    top_projects = Project.objects.order_by("-views", "-data", "title")[:5]

    return render(
        request,
        "orders/analytics.html",
        {
            "total": total_orders,
            "done": done_orders,
            "months": months,
            "top_pages": top_pages,
            "top_projects": top_projects,
        },
    )

def order_view(request):
    if request.method == "POST":
        form = OrderForm(request.POST)

        validator = validators.EmailValidator()
        if form.is_valid():
            
            try: 
                validator(form.cleaned_data["email"])
            except ValidationError:
                form.add_error("email", "Будь ласка, введіть дійсний email.")
                return render(request, "orders/order_form.html", {"form": form})

            order: Order = form.save()

            # Send confirmation email
            messge_client = render_to_string(
                "orders/email/confirmation.html", {"order": order}
            )
            send_mail(
                subject="дякуємо за ваше замовлення!",
                message="",
                from_email=settings.ADMIN_EMAIL,
                recipient_list=[order.email],
                html_message=messge_client,
            )

            # Send admin notification email
            message_admin = render_to_string(
                "orders/email/admin_notification.html", {"order": order}
            )
            send_mail(
                subject=f"Нове замовлення №{order.pk} від {order.name}",
                message="",
                from_email=settings.ADMIN_EMAIL,
                recipient_list=[settings.ADMIN_EMAIL],
                html_message=message_admin,
            )

            return redirect("order:success_view")

    form = OrderForm()
    return render(request, "orders/order_form.html", {"form": form})


def success_view(request):
    return render(request, "orders/success.html")
