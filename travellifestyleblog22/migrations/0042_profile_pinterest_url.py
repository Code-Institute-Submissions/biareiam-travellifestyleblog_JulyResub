# Generated by Django 3.2 on 2022-03-14 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travellifestyleblog22', '0041_auto_20220312_1145'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='pinterest_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
