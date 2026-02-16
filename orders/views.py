from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from .forms import OrderForm
from django.core.mail import send_mail
from .models import Order, PricingPackage, PageView, OrderAnalytics
from django.conf import settings
from django.core import validators
from django.core.exceptions import ValidationError
from django.db.models import Count
from datetime import datetime, timedelta

def pricing_view(request):
    packages = PricingPackage.objects.all()
    return render(request, "orders/pricing.html", {"packages": packages})

def analytics_view(request):
    total_orders = Order.objects.count()
    done_orders = Order.objects.filter(status="done").count()
    top_months = OrderAnalytics.objects.values('month').annotate(count=Count('month')).order_by('-count')[:6]
    return render(request, "orders/analytics.html", {"total": total_orders, "done": done_orders, "months": top_months})

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
