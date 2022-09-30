from django.db import models


class Vacancies(models.Model):
    title = models.CharField('Вакансия', max_length=255, blank=False)
    type_employment = models.CharField('Тип занятости', max_length=255, blank=True, null=True)
    city = models.CharField('Город', max_length=255, blank=True, null=True)
    description = models.TextField('Описание', null=True, blank=True)
    responsibilities = models.TextField('Обязанности', null=True, blank=True)
    requirements = models.TextField('Требования', null=True, blank=True)
    circumstances = models.TextField('Условия', null=True, blank=True)
    publish = models.BooleanField('Публикация', default=True)

    def __str__(self):
        return self.title
