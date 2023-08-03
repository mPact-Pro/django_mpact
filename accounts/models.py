from django.contrib.auth.models import AbstractUser
from agency.models import Agency
from django.db import models


# Creates a customer User model that behaves as the stock django model
# Difficult to change model after initial migration, this ensures
# That we can add fields as we need without having migration issues later
class User(AbstractUser):
    agency = models.ForeignKey(Agency, on_delete=models.SET_NULL, null=True)
    role = models.CharField(
        max_length=20,
        choices=[("admin", "Admin"), ("counselor", "Counselor")],
        null=True,
    )
