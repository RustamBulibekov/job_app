from django.db import models


# Create your models here.

class Vacancy(models.Model):
    title = models.CharField(max_length=30, verbose_name='Title', )
    description = models.TextField(verbose_name='Description about job')
    published = models.DateField(blank=True, null=True, verbose_name='Date_of_published')
    created_by = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    moderation = models.BooleanField(default=False, verbose_name='Moderation')

    class Meta:
        permissions = (
            ('can_moderation', 'Can moderation'),
        )

    def __str__(self):
        return self.title


class Resume(models.Model):
    title = models.CharField(max_length=30, verbose_name='Title', )
    description = models.TextField(verbose_name='Description')
    published = models.DateField(blank=True, null=True, verbose_name='Date_of_published')
    created_by = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    moderation = models.BooleanField(default=False)

    class Meta:
        permissions = (
            ('can_moderation', 'Can moderation'),
        )

    def __str__(self):
        return self.title
