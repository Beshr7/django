# Generated by Django 4.2.7 on 2023-11-27 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('targets', '0003_alter_target_model_target_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='target_model',
            name='new_field',
            field=models.IntegerField(default=0),
        ),
    ]
