from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class AppVacancyUser(AbstractUser):
    CHOICE_USER_STATUS = (
        ('look for job', 'employer',),
        ('look for employers', 'manager',)
    )
    date_of_birth = models.DateField(blank=True, null=True)
    city = models.CharField(max_length=20, )
    address = models.CharField(max_length=40, )
    status = models.CharField(max_length=20, choices=CHOICE_USER_STATUS)

    def __str__(self):
        return self.username
