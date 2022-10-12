from django.db import models


class Vacancies(models.Model):
    title = models.CharField('Вакансия', max_length=255, blank=False)
    type_employment = models.CharField('Тип занятости', max_length=255, blank=True, null=True)
    city = models.CharField('Город', max_length=255, blank=True, null=True)
    description = models.TextField('Описание', null=True, blank=True)
    publish = models.BooleanField('Публикация', default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вакансии'
        verbose_name_plural = 'Вакансии'


class Responsibilities(models.Model):
    vacancies = models.ForeignKey(Vacancies, related_name='responsibilities', on_delete=models.CASCADE)
    title = models.CharField('Обязанности', max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Обязанности'
        verbose_name_plural = 'Обязанности'


class Requirements(models.Model):
    vacancies = models.ForeignKey(Vacancies, related_name='requirements', on_delete=models.CASCADE)
    title = models.CharField('Требования', max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Требования'
        verbose_name_plural = 'Требования'


class Circumstances(models.Model):
    vacancies = models.ForeignKey(Vacancies, related_name='circumstances', on_delete=models.CASCADE)
    title = models.CharField('Условия', max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Условия'
        verbose_name_plural = 'Условия'


class VacanciesForm(models.Model):
    name = models.CharField('name', max_length=100)
    phone = models.CharField('phone', max_length=25)
    email = models.CharField('email', max_length=100)
    url = models.CharField('url', max_length=100)
    сhecked = models.BooleanField('сhecked', default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Форма вакансии'
        verbose_name_plural = 'Форма вакансии'
