# Generated by Django 3.1.7 on 2021-03-23 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='date',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='desc',
        ),
    ]
