# Generated by Django 5.0.1 on 2024-01-12 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificate_dapp', '0003_account_remove_profile_user_delete_todo_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('genre', models.CharField(max_length=200)),
                ('starring', models.CharField(max_length=350)),
            ],
        ),
        migrations.DeleteModel(
            name='Account',
        ),
    ]