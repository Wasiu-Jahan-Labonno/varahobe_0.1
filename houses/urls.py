from django.urls import path
from . import views

urlpatterns = [
    path('house_list', views.house_list, name='house_list'),
    path('create/', views.house_create, name='house_create'),
    path('houses/<int:pk>/', views.house_detail, name='house_detail'),

    path('edit/<int:pk>/', views.house_edit, name='house_edit'),


    path('delete/<int:pk>/', views.house_delete, name='house_delete'),
    path('houses/<int:pk>/contact/', views.contact_owner, name='contact_owner'),

]