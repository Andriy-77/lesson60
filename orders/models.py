from django.db import models

class PricingPackage(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    features = models.TextField()
    order = models.PositiveSmallIntegerField(default=0)
    class Meta:
        ordering = ["order"]

class PageView(models.Model):
    page_path = models.CharField(max_length=255)
    views = models.PositiveIntegerField(default=0)
    last_viewed = models.DateTimeField(auto_now=True)

class OrderAnalytics(models.Model):
    order = models.OneToOneField('Order', on_delete=models.CASCADE)
    month = models.CharField(max_length=7)
    count = models.PositiveIntegerField(default=0)

class Order(models.Model):
    STATUS_CHOICES = [
        ("new", "Нове замовлення"),
        ("in_progress", "В обробці"),
        ("done", "Завершено"),
        ("rejected", "Відхилено"),
    ]
    name = models.CharField(max_length=100)
    email = models.EmailField()
    project_description = models.TextField(verbose_name="Опис проекту")
    budget = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Бюджет (USD)"
    )
    deadline = models.CharField(max_length=100, verbose_name="Терміни реалізації")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="new")

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Замовлення"
        verbose_name_plural = "Замовлення"

    def __str__(self):
        return f"{self.pk}: Замовлення від {self.name} ({self.status})"
