from django.contrib.auth.models import AbstractUser


# Creates a customer User model that behaves as the stock django model
# Difficult to change model after initial migration, this ensures
# That we can add fields as we need without having migration issues later
class User(AbstractUser):
    pass