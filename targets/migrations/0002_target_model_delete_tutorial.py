# Generated by Django 4.2.7 on 2023-11-26 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('targets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Target_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=200)),
                ('target_id', models.TextField()),
                ('time_created', models.DateTimeField(verbose_name='date created')),
            ],
        ),
        migrations.DeleteModel(
            name='Tutorial',
        ),
    ]
