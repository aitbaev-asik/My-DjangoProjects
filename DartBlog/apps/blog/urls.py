from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeListView.as_view(), name='home'),
    path('category/<slug>', views.PostByCategoryListView.as_view(), name='category'),
    path('post/<slug>', views.PostDetailView.as_view(), name='post'),
    path('tag/<slug>', views.PostByTagListView.as_view(), name='tag'),
    path('search', views.SearchListView.as_view(), name='search'),
]
