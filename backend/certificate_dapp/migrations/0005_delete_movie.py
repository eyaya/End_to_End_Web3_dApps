# Generated by Django 5.0.1 on 2024-01-12 05:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('certificate_dapp', '0004_movie_delete_account'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Movie',
        ),
    ]