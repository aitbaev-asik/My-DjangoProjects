from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.create_todo, name='add'),
    path('edit/<int:pk>', views.complete_todo, name='complete'),
    path('delete_complete', views.delete_complete, name='deletecompleted'),
    path('delete_all', views.delete_all, name='deleteall')
]

