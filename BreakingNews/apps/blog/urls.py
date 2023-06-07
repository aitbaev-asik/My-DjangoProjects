from django.urls import path
from .views import index, news_detail, get_news_category, news_like, news_like_detail, search, news_dislike

urlpatterns = [
    path('', index, name='home'),
    path('news/<pk>', news_detail, name='news_detail'),
    path('category/<slug>', get_news_category, name='get_category'),
    path('like/<news_id>', news_like, name='news_like'),
    path('dislike/<news_id>', news_dislike, name='news_dislike'),
    path('like_a/<news_id>', news_like_detail, name='news_like_detail'),
    path('search', search, name='search'),
]

