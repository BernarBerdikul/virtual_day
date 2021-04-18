# Generated by Django 3.1.7 on 2021-04-18 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20210418_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='class_room',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Аудитория 1'), (1, 'Аудитория 2'), (2, 'Аудитория 3'), (3, 'Аудитория 4'), (4, 'Аудитория 5'), (5, 'Аудитория 6'), (6, 'Аудитория 7')], verbose_name='Дата дня'),
        ),
    ]
