from django.shortcuts import render, redirect

from .models import Comment
from apps.blog.models import Post


def create_comment(request, post_id):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        text = request.POST['text']
        post = Post.objects.get(id=post_id)

        Comment.objects.create(
            name=name,
            email=email,
            text=text,
            post=post
        )
        return redirect(f'/post/{post.slug}')

