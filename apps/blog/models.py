from django.db import models
from django.urls import reverse


# TODO: Страница блога
# TODO: Страница одного блога(читайте дальше)

class Blog(models.Model):
    title = models.CharField('Заголовок', max_length=255)
    slug = models.SlugField('slug', max_length=255, unique=True)
    description = models.CharField('Описание', max_length=255)
    image1 = models.ImageField('Главная картинка', upload_to='blog/', default='blog/no_image.jpg', null=True)
    text1 = models.TextField('Первая часть текста', null=True, blank=True)
    image2 = models.ImageField('Вторая картинка', upload_to='blog/', default='blog/no_image.jpg', null=True)
    text2 = models.TextField('Вторая часть текста', null=True, blank=True)
    image3 = models.ImageField('Третья картинка', upload_to='blog/', default='blog/no_image.jpg', null=True)
    publish = models.BooleanField('Публикация', default=True)
    main = models.BooleanField('Главная новость', default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блог'

    def get_absolute_url(self):
        return reverse('blog_single', kwargs={'slug_blog': self.slug})
