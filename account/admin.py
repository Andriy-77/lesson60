from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    """Адмінка для кастомного CustomUser"""

    model = CustomUser
    list_display = (    
        "username",
        "email",
        "first_name",
        "is_staff",
        "phone",
        "avatar",)

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name", "email")}),
        (
            "Додатковий профіль",
            {"fields": ("phone", "age", "github_profile", "avatar")},
        ),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "email",
                    "password1",
                    "password2",
                    "first_name",
                    "last_name",
                    "phone",
                    "age",
                    "github_profile",
                    "avatar",
                ),
            },
        ),
    )
