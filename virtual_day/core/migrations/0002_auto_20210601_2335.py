# Generated by Django 3.1.7 on 2021-06-01 17:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecture',
            name='speaker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Спикер'),
        ),
        migrations.AddField(
            model_name='event',
            name='dod_day',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.dodday', verbose_name='День ДОДа'),
        ),
        migrations.AddField(
            model_name='billboard',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.event', verbose_name='Событие'),
        ),
    ]
