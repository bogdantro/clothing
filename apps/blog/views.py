from .models import Post
from django.shortcuts import render, redirect
from django.views import generic
from django.shortcuts import render, get_object_or_404




def blog(request):
    post = Post.objects.filter(status=True)
    return render(request, 'core/blog.html', {'post':post})

def blog_post(request, title):
    post = get_object_or_404(Post, title=title)

    context = {
        'post':post
    }
    return render(request, 'core/blog_post.html', context)

