# Generated by Django 4.1 on 2022-10-03 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True, verbose_name='slug')),
                ('description', models.CharField(max_length=255, verbose_name='description')),
                ('text', models.TextField(blank=True, null=True, verbose_name='text')),
                ('image', models.ImageField(default='master_class_item/no_image.jpg', null=True, upload_to='master_class_item/', verbose_name='image')),
                ('publish', models.BooleanField(default=True, verbose_name='Публикация')),
            ],
            options={
                'verbose_name': 'Проекты',
                'verbose_name_plural': 'Проект',
            },
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True, verbose_name='slug')),
                ('description', models.CharField(max_length=255, verbose_name='description')),
            ],
            options={
                'verbose_name': 'Услуги',
                'verbose_name_plural': 'Услуга',
            },
        ),
    ]
