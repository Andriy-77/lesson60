from django.urls import path
from . import views

app_name = "order"

urlpatterns = [
    path("", views.order_view, name="order_view"),
    path("success/", views.success_view, name="success_view"),
    path("pricing/", views.pricing_view, name="pricing"),
    path("analytics/", views.analytics_view, name="analytics"),
]
