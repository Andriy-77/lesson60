from django.shortcuts import render, get_object_or_404
from .models import Project, Skill, Experience, BlogPost, Tag, Category, Comment
from django.db.models import Count

def blog_list(request):
    posts = BlogPost.objects.filter(published=True)
    category = request.GET.get('category')
    tag = request.GET.get('tag')
    if category:
        posts = posts.filter(category__slug=category)
    if tag:
        posts = posts.filter(tags__slug=tag)
    tags = Tag.objects.all()
    categories = Category.objects.all()
    return render(request, "portfolio/blog_list.html", {"posts": posts, "tags": tags, "categories": categories})

def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    post.views += 1
    post.save()
    comments = post.comments.filter(approved=True)
    return render(request, "portfolio/blog_detail.html", {"post": post, "comments": comments})

def popular_projects(request):
    projects = Project.objects.all()[:5]
    return render(request, "portfolio/popular_projects.html", {"projects": projects})

def index(request):
    projects = Project.objects.all()
    skills = Skill.objects.all()
    experiences = Experience.objects.all()

    context = {
        "projects": projects,
        "skills": skills,
        "experiences": experiences,
    }
    return render(request, "portfolio/index.html", context)
