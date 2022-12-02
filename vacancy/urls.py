from django.urls import path
from .views import VacancyListView, ResumeListView, CreateVacancyView, CreateResumeView

app_name = 'vacancy'

urlpatterns = [
    path('resume/', ResumeListView.as_view(), name='resume_list', ),
    path('vacancy_list/', VacancyListView.as_view(), name='vacancy_list', ),
    path('add_vacancy/', CreateVacancyView.as_view(), name='add_vacancy'),
    path('add_resume/', CreateResumeView.as_view(), name='add_resume'),
]
