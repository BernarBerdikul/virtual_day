# Generated by Django 3.1.7 on 2021-04-18 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20210418_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='event',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='lecture', to='core.event', verbose_name='Событие'),
        ),
    ]