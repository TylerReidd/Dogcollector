# Generated by Django 3.0.8 on 2020-10-08 20:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='cat',
            new_name='dog',
        ),
    ]
