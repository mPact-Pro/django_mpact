from django.db import models

from agency.models import Agency

# Create your models here.


class Service(models.Model):
    name = models.CharField(max_length=200, null=True)
    addedOn = models.DateTimeField(auto_now_add=True)
    updatedOn = models.DateTimeField(auto_now=True)
    serviceDate = models.DateField(db_index=True)
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"

    def __str__(self) -> str:
        return f"{self.name}"
