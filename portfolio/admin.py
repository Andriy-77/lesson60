from django.contrib import admin
from .models import Project, Skill, Experience, BlogPost, Tag, Category, Comment

@admin.register(BlogPost)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "created_at", "published", "views")
    list_filter = ("published", "category")
    search_fields = ("title", "content")
    prepopulated_fields = {"slug": ("title",)}

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("author", "post", "created_at", "approved")
    list_filter = ("approved",)
    search_fields = ("author", "email", "content", "post__title")

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "data", "views", "github_url")
    list_filter = ("data",)
    search_fields = ("title", "technologies")
    readonly_fields = ()


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "level", "category")
    list_filter = ("category",)
    search_fields = ("name",)


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("position", "company", "start_date", "end_date")
    list_filter = ("company",)
    search_fields = ("position", "company")
