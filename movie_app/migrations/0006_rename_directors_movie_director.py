# Generated by Django 5.0.1 on 2024-02-28 07:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0005_alter_review_stars'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='directors',
            new_name='director',
        ),
    ]
