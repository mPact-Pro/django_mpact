from django.contrib.auth.models import AbstractUser
from agency.models import Agency
from django.db import models


# Creates a customer User model that behaves as the stock django model
# Difficult to change model after initial migration, this ensures
# That we can add fields as we need without having migration issues later
# A user can be assigned to an agency
# A user can be assigned a role: Admin, Counselor
# We will be able to add, update set default roles and permissions here as well
class User(AbstractUser):
    agency = models.ForeignKey(
        Agency, on_delete=models.SET_NULL, null=True, db_index=True, default='1')
    role = models.CharField(
        max_length=20,
        choices=[("admin", "Admin"), ("counselor", "Counselor")],
        null=True,
    )
