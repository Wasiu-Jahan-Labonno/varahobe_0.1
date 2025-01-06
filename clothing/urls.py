from django.urls import path
from . import views

urlpatterns = [
    path('clothing_list', views.clothing_list, name='clothing_list'),
    path('create/', views.clothing_create, name='clothing_create'),
    path('edit/<int:pk>/', views.clothing_edit, name='clothing_edit'),
    path('clothing/<int:pk>/', views.clothing_detail, name='clothing_detail'),
    path('delete/<int:pk>/', views.clothing_delete, name='clothing_delete'),
]