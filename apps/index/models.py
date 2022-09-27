from django.db import models


class IndexForm(models.Model):
    name = models.CharField('name', max_length=255)
    phone = models.TextField('phone', max_length=16)

    def __str__(self):
        return self.name
