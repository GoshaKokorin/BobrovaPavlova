from django.db import models


class IndexForm(models.Model):
    name = models.CharField('name', max_length=100)
    phone = models.CharField('phone', max_length=25)
    # date = models.DateTimeField('date', auto_now_add=True)
    сhecked = models.BooleanField('сhecked', default=False)

    def __str__(self):
        return self.name
