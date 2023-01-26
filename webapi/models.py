from django.db import models


class Terms(models.Model):
    term = models.CharField('Термин', max_length=100)
    description = models.TextField('Описание')

    def __str__(self):
        return self.term

    class Meta:
        verbose_name = 'Термин'
        verbose_name_plural = 'Термины'



