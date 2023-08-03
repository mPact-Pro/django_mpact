from django.db import models

# Create your models here.


class Service(models.Model):
    name = models.CharField(max_length=200, null=True)

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self) -> str:
        return f'{self.name}'
