# Generated by Django 3.2 on 2022-02-23 22:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('travellifestyleblog22', '0016_alter_post_featured_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='title_tag',
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(default='Movies', max_length=255),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/profile/')),
                ('instagram_url', models.CharField(blank=True, max_length=255, null=True)),
                ('facebook_url', models.CharField(blank=True, max_length=255, null=True)),
                ('first_name', models.CharField(default='Mary', max_length=255)),
                ('last_name', models.CharField(default='Ann', max_length=255)),
                ('email', models.EmailField(default='my@email.com', max_length=254)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('date_addded', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='travellifestyleblog22.post')),
            ],
            options={
                'ordering': ['-date_addded'],
            },
        ),
    ]