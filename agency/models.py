from django.db import models

# Create your models here.


class Agency(models.Model):
    name = models.CharField(max_length=200, null=True)

    class Meta:
        verbose_name = 'Agency'
        verbose_name_plural = 'Agencies'

    def __str__(self) -> str:
        return f'{self.name}'
