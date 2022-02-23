# Generated by Django 3.2 on 2022-02-23 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travellifestyleblog22', '0003_auto_20220223_1003'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default='Life Style', max_length=255),
        ),
    ]