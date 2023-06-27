from django.contrib import admin
from users.models import CustomUser


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'password']
    search_fields = ['email'],
    list_per_page = 10


admin.site.register(CustomUser, UserAdmin)
