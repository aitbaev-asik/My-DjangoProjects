from django.urls import path
from . import views

urlpatterns = [
    path('create_like/<post_id>', views.create_like_post, name='create_like_post'),
]
