# Generated by Django 3.2.4 on 2021-06-11 00:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_profile', '0014_rename_siblings_sibling'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='language',
            name='number_of_languages',
        ),
    ]
