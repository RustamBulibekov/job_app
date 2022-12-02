from django.urls import path
from .views import UserLoginInView, UserLogOutView, register

app_name = 'user'

urlpatterns = [
    path('registration/', register, name='registration', ),
    path('login/', UserLoginInView.as_view(), name='login', ),
    path('logout/', UserLogOutView.as_view(), name='logout', ),

]
