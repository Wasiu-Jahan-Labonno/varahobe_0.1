from django.urls import path
from . import views

urlpatterns = [
    path('', views.house_list, name='house_list'),
    path('create/', views.house_create, name='house_create'),
    path('edit/<int:pk>/', views.house_edit, name='house_edit'),
    path('delete/<int:pk>/', views.house_delete, name='house_delete'),
]