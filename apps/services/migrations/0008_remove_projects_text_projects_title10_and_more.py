# Generated by Django 4.1 on 2022-10-06 21:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0007_alter_projects_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='text',
        ),
        migrations.AddField(
            model_name='projects',
            name='title10',
            field=models.CharField(max_length=255, null=True, verbose_name='Заголовок 2'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='image2',
            field=models.ImageField(default='project/no_image.jpg', null=True, upload_to='project/', verbose_name='Картинка 2'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='image3',
            field=models.ImageField(default='project/no_image.jpg', null=True, upload_to='project/', verbose_name='Картинка 3'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='image4',
            field=models.ImageField(default='project/no_image.jpg', null=True, upload_to='project/', verbose_name='Картинка 4'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='image5',
            field=models.ImageField(default='project/no_image.jpg', null=True, upload_to='project/', verbose_name='Картинка 5'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='image6',
            field=models.ImageField(default='project/no_image.jpg', null=True, upload_to='project/', verbose_name='Картинка 6'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='image7',
            field=models.ImageField(default='project/no_image.jpg', null=True, upload_to='project/', verbose_name='Картинка 7'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='image8',
            field=models.ImageField(default='project/no_image.jpg', null=True, upload_to='project/', verbose_name='Картинка 8'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='image9',
            field=models.ImageField(default='project/no_image.jpg', null=True, upload_to='project/', verbose_name='Картинка 9'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='main',
            field=models.BooleanField(default=False, verbose_name='Показывать на странице проекта'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='services_project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='services_project', to='services.services', verbose_name='Услуга'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, unique=True, verbose_name='Не изменять'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='title2',
            field=models.CharField(max_length=255, null=True, verbose_name='Заголовок 1'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='title3',
            field=models.CharField(max_length=255, null=True, verbose_name='Приписка к картинке 6'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='title4',
            field=models.CharField(max_length=255, null=True, verbose_name='Приписка к картинке 7'),
        ),
        migrations.AlterField(
            model_name='services',
            name='description',
            field=models.CharField(max_length=255, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='services',
            name='image1',
            field=models.ImageField(default='services/no_image.jpg', null=True, upload_to='services/', verbose_name='Картинка 1'),
        ),
        migrations.AlterField(
            model_name='services',
            name='image2',
            field=models.ImageField(default='services/no_image.jpg', null=True, upload_to='services/', verbose_name='Картинка 2'),
        ),
        migrations.AlterField(
            model_name='services',
            name='image3',
            field=models.ImageField(default='services/no_image.jpg', null=True, upload_to='services/', verbose_name='Картинка 3'),
        ),
        migrations.AlterField(
            model_name='services',
            name='image4',
            field=models.ImageField(default='services/no_image.jpg', null=True, upload_to='services/', verbose_name='Картинка 4'),
        ),
        migrations.AlterField(
            model_name='services',
            name='image5',
            field=models.ImageField(default='services/no_image.jpg', null=True, upload_to='services/', verbose_name='Картинка 5'),
        ),
        migrations.AlterField(
            model_name='services',
            name='image6',
            field=models.ImageField(default='services/no_image.jpg', null=True, upload_to='services/', verbose_name='Картинка 6'),
        ),
        migrations.AlterField(
            model_name='services',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Название услуги'),
        ),
    ]
