from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import AppVacancyUser


class CreateAppVacancyUser(UserCreationForm):
    # username = forms.CharField(label='username', min_length=5, max_length=150)
    # email = forms.EmailField(label='email')
    # password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    # password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)
    # first_name = forms.CharField(max_length=30, required=False, help_text='FirstName')
    # last_name = forms.CharField(max_length=30, required=False, help_text='lastName')
    # date_of_birth = forms.DateField(required=True, help_text='date of birth')
    # city = forms.CharField(required=False, help_text='Select you town')
    # address = forms.CharField(required=True, help_text='Your address')
    # status = forms.ChoiceField(help_text='choice your status')

    class Meta:
        model = AppVacancyUser
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2','date_of_birth', 'address','city', 'status',)
