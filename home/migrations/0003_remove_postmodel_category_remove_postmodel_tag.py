# Generated by Django 4.2.3 on 2023-07-10 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postmodel',
            name='category',
        ),
        migrations.RemoveField(
            model_name='postmodel',
            name='tag',
        ),
    ]
