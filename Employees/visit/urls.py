from django.urls import path
from . import views


urlpatterns = [
    path('', views.visit_list, name='visit_list'),
    path('visit/new/', views.visit_new, name='visit_new'),
    path('visit/', views.Visit, name='visit'),
    path('delete/<int:id>', views.visit_delete, name='delete_visit'),
    path('edit/<int:id>', views.visit_edit, name='edit_visit'),
]

