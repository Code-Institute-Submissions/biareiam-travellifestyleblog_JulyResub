# Generated by Django 3.2 on 2022-03-06 10:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travellifestyleblog22', '0030_remove_comment_comment_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-date_addded']},
        ),
        migrations.RemoveField(
            model_name='comment',
            name='date_addded',
        ),
        migrations.AddField(
            model_name='comment',
            name='date_addded',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_on',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
