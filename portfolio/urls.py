from django.urls import path
from . import views

app_name = "portfolio"

urlpatterns = [
    path("", views.index, name="index"),
    path("projects/<int:pk>/", views.project_detail, name="project_detail"),
    path("blog/", views.blog_list, name="blog_list"),
    path("blog/<slug:slug>/", views.blog_detail, name="blog_detail"),
    path("popular/", views.popular_projects, name="popular_projects"),
]
