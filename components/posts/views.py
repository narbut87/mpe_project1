from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import PostForm
from .models import Group, Post


def index(request):
    latest = Post.objects.all()[:11]
    return render(request, 'posts/index.html', {'posts': latest})


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.group_posts.all()[:12]
    return render(request, 'group.html', {'group': group, 'posts': posts})


@login_required
def new_post(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return redirect('index')
    return render(request, 'posts/new.html', {'form': form})


def catalog(request):
    return render(request, 'catalog.html')
