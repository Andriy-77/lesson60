from django.contrib import admin
from .models import Order, PricingPackage, PageView, OrderAnalytics

@admin.register(PricingPackage)
class PricingAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "order")

@admin.register(PageView)
class PageViewAdmin(admin.ModelAdmin):
    list_display = ("page_path", "views", "last_viewed")
    readonly_fields = ("page_path", "views", "last_viewed")

@admin.register(OrderAnalytics)
class AnalyticsAdmin(admin.ModelAdmin):
    list_display = ("order", "month", "count")

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "budget", "deadline", "status", "created_at")
    list_filter = ("status", "created_at")
    search_fields = ("name", "email", "project_description")
    readonly_fields = ("created_at",)

    # відображення полів у формі адміністратора
    fieldsets = (
        (
            "main",
            {"fields": ("name", "email", "project_description", "budget", "deadline")},
        ),
        ("Status Information", {"fields": ("status", "created_at")}),
    )
    ordering = ["-created_at"]
