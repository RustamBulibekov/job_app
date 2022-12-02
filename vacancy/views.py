from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView, CreateView
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import Vacancy, Resume
from .forms import VacancyForm, ResumeForm


# Create your views here.


class VacancyListView(PermissionRequiredMixin,ListView):
    permission_required = ['vacancy.view_vacancy', ]
    template_name = 'vacancy_list.html'
    model = Vacancy
    context_object_name = 'vacancy'

    def get_queryset(self):
        return Vacancy.objects.filter(moderation=True)


class ResumeListView(PermissionRequiredMixin, ListView):
    permission_required = ('vacancy.view_resume', 'vacancy.add_resume', 'vacancy.change_resume',
                           'vacancy.delete_resume', 'vacancy.view_vacancy', )
    template_name = 'resume_list.html'
    model = Resume
    context_object_name = 'resume'

    def get_queryset(self):
        return Resume.objects.filter(moderation=True)


class CreateVacancyView(PermissionRequiredMixin, CreateView):
    form_class = VacancyForm
    template_name = 'create_vacancy.html'
    success_url = '/'
    permission_required = ['app_vacancy.add_vacancy']


class CreateResumeView(CreateView):
    form_class = ResumeForm
    template_name = 'create_resume.html'
    success_url = '/'
    # permission_required = ['app_vacancy.view_resume']
