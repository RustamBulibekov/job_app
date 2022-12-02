from django.contrib import admin
from .models import AppVacancyUser


# Register your models here.


@admin.register(AppVacancyUser)
class UserAdminModel(admin.ModelAdmin):
    list_display = ['id', 'username', 'is_active', 'is_staff']
