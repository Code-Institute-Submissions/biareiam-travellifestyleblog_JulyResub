# Generated by Django 3.2 on 2022-02-23 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travellifestyleblog22', '0020_auto_20220223_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(default=' ', max_length=254),
        ),
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(default=' ', max_length=255),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(default=' ', max_length=255),
        ),
    ]