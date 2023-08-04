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

    def get_all_users(self):
        # Retrieve all agency users counselors and admins
        return self.user_set.all()

    def get_all_customers(self):
        # Retrieve all customers associated with this agency
        return self.customer_set.all()

    def get_all_courses(self):
        # Retrieve all courses associated with this agency
        return self.course_set.all()
