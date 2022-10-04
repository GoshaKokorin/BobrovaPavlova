from django.db import models


class Services(models.Model):
    title = models.CharField('title', max_length=255)
    slug = models.SlugField('slug', max_length=255, blank=True, unique=True)
    description = models.CharField('description', max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def get_absolute_url(self):
        return '/services/%s/' % self.slug


class Projects(models.Model):
    title = models.CharField('Заголовок', max_length=255)
    description = models.CharField('Краткое описание', max_length=255, null=True)
    description2 = models.CharField('Краткое описание 2', max_length=255, null=True)
    description3 = models.CharField('Площадь', max_length=255, null=True)
    description4 = models.CharField('Город', max_length=255, null=True)
    description5 = models.CharField('Архитекторы', max_length=255, null=True)
    title2 = models.CharField('Заголовок 2', max_length=255, null=True)
    description6 = models.CharField('Краткое описание 2', max_length=255, null=True)
    title3 = models.CharField('Приписка к проекту', max_length=255, null=True)
    title4 = models.CharField('Заголовок 2', max_length=255, null=True)
    title5 = models.CharField('Заголовок 2', max_length=255, null=True)
    image1 = models.ImageField('Главная картинка', upload_to='project/', default='project/no_image.jpg',
                               null=True)
    image2 = models.ImageField('Главная картинка', upload_to='project/', default='project/no_image.jpg',
                               null=True)
    image3 = models.ImageField('Главная картинка', upload_to='project/', default='project/no_image.jpg',
                               null=True)
    image4 = models.ImageField('Главная картинка', upload_to='project/', default='project/no_image.jpg',
                               null=True)
    image5 = models.ImageField('Главная картинка', upload_to='project/', default='project/no_image.jpg',
                               null=True)
    image6 = models.ImageField('Главная картинка', upload_to='project/', default='project/no_image.jpg',
                               null=True)
    image7 = models.ImageField('Главная картинка', upload_to='project/', default='project/no_image.jpg',
                               null=True)
    image8 = models.ImageField('Главная картинка', upload_to='project/', default='project/no_image.jpg',
                               null=True)
    image9 = models.ImageField('Главная картинка', upload_to='project/', default='project/no_image.jpg',
                               null=True)
    text = models.TextField('Текст', null=True, blank=True)
    publish = models.BooleanField('Публикация', default=True)
    main = models.BooleanField('На главной', default=False)
    slug = models.SlugField('slug', max_length=255, blank=True, unique=True)
    # services = models.ForeignKey(Services, related_name='services_project', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    # def get_absolute_url(self):
    #     return '/services/%s/%s/' % self.services.slug % self.slug
