# Generated by Django 2.2 on 2022-11-19 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancy', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='resume',
            options={'permissions': (('can_moderation', 'Can moderation'),)},
        ),
        migrations.AlterModelOptions(
            name='vacancy',
            options={'permissions': (('can_moderation', 'Can moderation'),)},
        ),
        migrations.AddField(
            model_name='resume',
            name='moderation',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='moderation',
            field=models.BooleanField(default=False, verbose_name='Moderation'),
        ),
    ]