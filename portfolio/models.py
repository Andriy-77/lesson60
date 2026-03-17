from django.db import models
from django.conf import settings

class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    class Meta:
        verbose_name_plural = "Categories"
    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    content = models.TextField()
    excerpt = models.CharField(max_length=300, blank=True)
    image = models.ImageField(upload_to="blog/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=True)
    views = models.PositiveIntegerField(default=0)
    class Meta:
        ordering = ["-created_at"]
    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name="comments")
    author = models.CharField(max_length=100)
    email = models.EmailField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.author}"

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technologies = models.CharField(
        max_length=300, help_text="через кому: Python, JS, Postgres"
    )
    data = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to="projects/", null=True, blank=True)
    github_url = models.URLField(null=True, blank=True)
    views = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["-data", "title"]
        verbose_name = "Проект"
        verbose_name_plural = "Проекти"

    def __str__(self) -> str:
        return self.title


class Skill(models.Model):
    CATEGORY_CHOISE = [
        ("soft", "Soft"),
        ("frontend", "Frontend"),
        ("backend", "Backend"),
        ("devops", "DevOps"),
    ]

    name = models.CharField(max_length=100)
    level = models.PositiveSmallIntegerField(default=50, help_text="0-100")  # 0-100
    category = models.CharField(
        max_length=20, choices=CATEGORY_CHOISE, default="backend"
    )

    class Meta:
        ordering = ["-level", "name"]
        verbose_name = "Навик"
        verbose_name_plural = "Навички"

    def __str__(self) -> str:
        return f"[{self.name}]: {self.level}"


class Experience(models.Model):
    position = models.CharField(max_length=120)
    company = models.CharField(max_length=120)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ["-start_date", "company"]
        verbose_name = "Досвід"
        verbose_name_plural = "Досвід"

    def __str__(self) -> str:
        period = (
            f"{self.start_date} - {self.end_date}"
            if self.end_date
            else f"{self.start_date} - Present"
        )
        return f"[{self.position}] in {self.company} ({period})"
