# Generated by Django 3.2.4 on 2021-06-11 00:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_profile', '0013_siblings'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Siblings',
            new_name='Sibling',
        ),
    ]
