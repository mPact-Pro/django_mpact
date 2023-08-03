from django.db import models

# Create your models here.


# Base Agency table, Every user will be assigned an agency
# Each customer will only be available to that agency
# Each customers sessions, services, or courses will only
# be available to that users agency
# Basis of multi-tenency for the frontend application
class Agency(models.Model):
    name = models.CharField(max_length=200, null=True)

    class Meta:
        verbose_name = "Agency"
        verbose_name_plural = "Agencies"

    def __str__(self) -> str:
        return f"{self.name}"
