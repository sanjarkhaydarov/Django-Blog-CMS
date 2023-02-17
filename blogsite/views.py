from django.shortcuts import render
from .models import Post


def index(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'blogsite/index.html', context)

def detail(request, slug):
    post = Post.objects.get(slug=slug)
    posts = Post.objects.exclude(post_id__exact=post.post_id)[:5]
    context = {'post': post, 'posts': posts}
    return render (request, 'blogsite/detail.html', context)