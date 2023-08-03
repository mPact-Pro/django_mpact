from django.db import models
from agency.models import Agency

from courses.models import CourseClass
from services.models import Service
from mPactSessions.models import Session

# Create your models here.

# An agency can have multiple customers per the ForeignKey assignment
# A Class can have many customers, and a customer can have many classes
# A customer can have many sessions, and services


class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField()
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE)
    courseClass = models.ManyToManyField(CourseClass, blank=True)
    sessions = models.ForeignKey(Session, blank=True)
    services = models.ManyToManyField(Service, blank=True)
    addedOn = models.DateTimeField(auto_now_add=True)
    updatedOn = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"

    def __str__(self) -> str:
        return f"{self.name}"
