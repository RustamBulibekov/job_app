from django.shortcuts import render, redirect, reverse
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.auth.models import Group
from django.contrib.auth import login, authenticate
from .forms import CreateAppVacancyUser


# Create your views here.


class UserLoginInView(LoginView):
    template_name = 'login.html'


class UserLogOutView(LogoutView):
    next_page = '/'


def register(request):
    if request.method == 'POST':
        form = CreateAppVacancyUser(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            row_password = form.cleaned_data.get('password1')
            group = form.cleaned_data.get('status')
            user = authenticate(username=username, password=row_password)
            user = form.save()
            if group == 'look for job':
                gr_job = Group.objects.get(name='Employers')
                user.groups.add(gr_job)
                user.save()
            elif group == 'look for employers':
                gr_job = Group.objects.get(name='Manager')
                user.groups.add(gr_job)
                user.save()

            login(request, user)
            return redirect('/')
    else:
        form = CreateAppVacancyUser()
    return render(request, 'registration.html', {'form': form})
