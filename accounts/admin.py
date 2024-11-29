from django.contrib import admin
from .models import User
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'user_type', 'email', 'is_staff', 'is_active')
    list_filter = ('user_type', 'is_staff', 'is_active')