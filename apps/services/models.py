# from django.db import models
#
#
# class Services(models.Model):
#     title = models.CharField('title', max_length=255)
#     slug = models.SlugField('slug', max_length=255, blank=True, unique=True)
#     description = models.CharField('description', max_length=255)
#
#     def __str__(self):
#         return self.title
#
#     class Meta:
#         verbose_name = 'Услуги'
#         verbose_name_plural = 'Услуга'
#
#     def get_absolute_url(self):
#         return '/services/%s/' % self.slug
#
#
# class Projects(models.Model):
#     title = models.CharField('title', max_length=255)
#     slug = models.SlugField('slug', max_length=255, blank=True, unique=True)
#     description = models.CharField('description', max_length=255)
#     text = models.TextField('text', null=True, blank=True)
#     image = models.ImageField('image', upload_to='master_class_item/', default='master_class_item/no_image.jpg',
#                               null=True)
#     publish = models.BooleanField('Публикация', default=True)
#
#     def __str__(self):
#         return self.title
#
#     class Meta:
#         verbose_name = 'Проекты'
#         verbose_name_plural = 'Проект'
#
#     def get_absolute_url(self):
#         return '/services/%s/' % self.slug
