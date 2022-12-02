from django import forms
from .models import Vacancy, Resume


class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ['title', 'description', ]


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['title', 'description', ]
