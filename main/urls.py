from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect
from django.urls import path
from houses import views as home

urlpatterns = [
    path('', home.home, name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('houses/', include('houses.urls')),
    path('', lambda request: redirect('house_list')),
    path('houses/', home.house_list, name='house_list'),
    path('house/create/', home.house_create, name='house_create'),
    path('house/edit/<int:pk>/', home.house_edit, name='house_edit'),
    path('house/delete/<int:pk>/', home.house_delete, name='house_delete'),





    # Redirect root URL to house_list view
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
