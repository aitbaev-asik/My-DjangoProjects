from django.shortcuts import render, redirect
from .models import PostLike
from ..blog.models import Post

def create_like_post(request, post_id):
    post = Post.objects.get(id=post_id)
    like = PostLike.objects.get(post__id=post_id, user=request.user)
    if like.exists():
        like.delete()
    else:
        PostLike.objects.create(
            user=request.user, post=post
        )
    return redirect(f'/post/{post.slug}')


