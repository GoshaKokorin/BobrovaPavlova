from django.db import models
from django.urls import reverse


class Services(models.Model):
    title = models.CharField('Название услуги', max_length=255)
    slug = models.SlugField('Не изменять', max_length=255, blank=True, null=True, unique=True)
    description = models.CharField('Описание', max_length=255)
    image1 = models.ImageField('Картинка 1', upload_to='services/', default='services/no_image.jpg', null=True)
    image2 = models.ImageField('Картинка 2', upload_to='services/', default='services/no_image.jpg', null=True)
    image3 = models.ImageField('Картинка 3', upload_to='services/', default='services/no_image.jpg', null=True)
    image4 = models.ImageField('Картинка 4', upload_to='services/', default='services/no_image.jpg', null=True)
    image5 = models.ImageField('Картинка 5', upload_to='services/', default='services/no_image.jpg', null=True)
    image6 = models.ImageField('Картинка 6', upload_to='services/', default='services/no_image.jpg', null=True)
    image7 = models.ImageField('Картинка 7', upload_to='services/', default='services/no_image.jpg', null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def get_absolute_url(self):
        return reverse('single_services', kwargs={'slug_service': self.slug})


class Projects(models.Model):
    image1 = models.ImageField('Главная картинка', upload_to='project/', default='project/no_image.jpg', null=True)
    title = models.CharField('Название проекта', max_length=255)
    slug = models.SlugField('Не изменять', max_length=255, blank=True, unique=True)
    description = models.CharField('Краткое описание проекта', max_length=255, null=True)
    image2 = models.ImageField('Картинка 2', upload_to='project/', default='project/no_image.jpg', null=True)
    image3 = models.ImageField('Картинка 3', upload_to='project/', default='project/no_image.jpg', null=True)
    image4 = models.ImageField('Картинка 4', upload_to='project/', default='project/no_image.jpg', null=True)
    description2 = models.CharField('Текст 1', max_length=255, null=True)
    description3 = models.CharField('Площадь', max_length=255, null=True)
    description4 = models.CharField('Город', max_length=255, null=True)
    description5 = models.CharField('Архитекторы', max_length=255, null=True)
    title2 = models.CharField('Заголовок 2', max_length=255, null=True)
    description6 = models.CharField('Текст к заголовку 2', max_length=500, null=True)
    image5 = models.ImageField('Картинка 5', upload_to='project/', default='project/no_image.jpg', null=True)
    image6 = models.ImageField('Картинка 6', upload_to='project/', default='project/no_image.jpg', null=True)
    title3 = models.CharField('Приписка к картинке 6', max_length=255, null=True)
    image7 = models.ImageField('Картинка 7', upload_to='project/', default='project/no_image.jpg', null=True)
    title4 = models.CharField('Приписка к картинке 7', max_length=255, null=True)
    image8 = models.ImageField('Картинка 8', upload_to='project/', default='project/no_image.jpg', null=True)
    title5 = models.CharField('Приписка к картинке 8', max_length=255, null=True)
    title6 = models.CharField('Заголовок 3', max_length=255, null=True)
    title7 = models.CharField('Текст к заголовку 3', max_length=500, null=True)
    title9 = models.CharField('Заголовок 4', max_length=255, null=True)
    title10 = models.CharField('Текст к заголовку 4', max_length=500, null=True)
    image9 = models.ImageField('Картинка 9', upload_to='project/', default='project/no_image.jpg', null=True)
    title8 = models.CharField('Приписка к картинке 9', max_length=255, null=True)
    year = models.CharField('Год проекта', max_length=255, null=True)
    publish = models.BooleanField('Публикация', default=True)
    main = models.BooleanField('Показывать на странице проекта', default=False)
    services_project = models.ForeignKey(Services, related_name='services_project', on_delete=models.CASCADE,
                                         blank=True, null=True, verbose_name='Услуга')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def get_absolute_url(self):
        return reverse('services_project',
                       kwargs={'slug_service': self.services_project.slug, 'slug_project': self.slug})
