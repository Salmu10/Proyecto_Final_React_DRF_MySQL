# Generated by Django 4.1.5 on 2023-02-13 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='biography',
            field=models.CharField(blank=True, default="Hello, I'm a dreamhouse user", max_length=100),
        ),
    ]
