# Generated by Django 4.2.7 on 2023-11-27 13:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flowless', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pressure_sensor',
            name='installation_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 27, 16, 14, 18, 691949), verbose_name='date created'),
        ),
        migrations.AddField(
            model_name='pressure_sensor',
            name='label',
            field=models.CharField(default='default', max_length=200),
        ),
        migrations.AddField(
            model_name='pressure_sensor',
            name='latitude',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pressure_sensor',
            name='longitude',
            field=models.IntegerField(default=0),
        ),
    ]
