from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    phone = models.CharField(
        max_length=20, blank=True, null=True, verbose_name="Номер телефону"
    )
    age = models.PositiveIntegerField(blank=True, null=True, verbose_name="Вік")
    github_profile = models.URLField(
        max_length=200, blank=True, null=True, verbose_name="GitHub профіль"
    )

    avatar = models.ImageField(
        default="avatars/default_avatar.png",
        upload_to="avatars/",
        null=True,
        blank=True,
        verbose_name="Аватар",
    )

    def __str__(self) -> str:
        return f"{self.pk}: {self.username}"
