# Generated by Django 4.2.8 on 2024-01-23 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_suspended',
            field=models.BooleanField(default=False),
        ),
    ]