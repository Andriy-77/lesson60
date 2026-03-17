from django.shortcuts import render, get_object_or_404, redirect
from .models import Project, Skill, Experience, BlogPost, Tag, Category, Comment
from django.db.models import Count, F
from .forms import CommentForm

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
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment: Comment = form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            return redirect("portfolio:blog_detail", slug=post.slug)
    else:
        form = CommentForm()

    return render(
        request,
        "portfolio/blog_detail.html",
        {"post": post, "comments": comments, "form": form},
    )

def popular_projects(request):
    projects = Project.objects.order_by("-views", "-data", "title")[:5]
    return render(request, "portfolio/popular_projects.html", {"projects": projects})

def project_detail(request, pk: int):
    project = get_object_or_404(Project, pk=pk)
    Project.objects.filter(pk=project.pk).update(views=F("views") + 1)
    project.refresh_from_db(fields=["views"])
    return render(request, "portfolio/project_detail.html", {"project": project})

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
