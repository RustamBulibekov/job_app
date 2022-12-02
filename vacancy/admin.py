from django.contrib import admin
from .models import Resume, Vacancy


# Register your models here.


@admin.register(Vacancy)
class VacancyAdminModel(admin.ModelAdmin):
    list_display = ['id', 'title', ]


@admin.register(Resume)
class ResumeAdminModel(admin.ModelAdmin):
    list_display = ['id', 'title']
