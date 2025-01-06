from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect
from django.urls import path

from clothing  import views as  clot
from houses import views as home

urlpatterns = [
    path('', home.home, name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('houses/', include('houses.urls')),
    path('', lambda request: redirect('house_list')),
    path('allhouse/', home.allhouse, name='allhouse'),
    path('houses/', home.house_list, name='house_list'),
    path('house/create/', home.house_create, name='house_create'),
    path('houses/<int:pk>/', home.house_detail, name='house_detail'),
    path('house/edit/<int:pk>/', home.house_edit, name='house_edit'),
    path('house/delete/<int:pk>/', home.house_delete, name='house_delete'),
    path('allclothing/', clot.clothing, name='clothing'),
    path('clothing/', clot.clothing_list, name='clothing_list'),
    path('clothing/create/', clot.clothing_create, name='clothing_create'),
    path('clothing/<int:pk>/', clot.clothing_detail, name='clothing_detail'),
    path('clothing/edit/<int:pk>/', clot.clothing_edit, name='clothing_edit'),
    path('clothing/delete/<int:pk>/', clot.clothing_delete, name='clothing_delete'),






    # Redirect root URL to house_list view
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
