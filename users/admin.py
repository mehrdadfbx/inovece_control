from django.contrib import admin

from users.models import User

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'display_name', 'phone', 'role', 'is_active', 'created_by', 'last_login', 'created_at', 'updated_at')
    list_filter = ('role', 'is_active')
    search_fields = ('username', 'display_name', 'phone')
    ordering = ('username',)

admin.site.register(User, UserAdmin)