# Generated by Django 5.0.1 on 2024-01-10 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificate_dapp', '0002_todo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=58)),
                ('private_key', models.CharField(max_length=90)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Todo',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
