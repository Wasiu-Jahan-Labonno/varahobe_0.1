from django.contrib import admin

from .models import House
# Register your models here.
from django.contrib import admin
from .models import House

@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'price', 'area', 'address', 'image_preview')
    list_filter = ('area', 'owner')
    search_fields = ('title', 'description', 'address', 'area')
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" style="max-width: 100px; height: auto;">'
        return "No image available"
    image_preview.allow_tags = True
    image_preview.short_description = 'Image Preview'
