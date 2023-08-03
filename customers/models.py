from django.db import models
from agency.models import Agency

from courses.models import Course, CourseClass
from services.models import Service
from mPactSessions.models import Session

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField()
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Course, blank=True)
    courseClass = models.ManyToManyField(CourseClass, blank=True)
    sessions = models.ManyToManyField(Session, blank=True)
    services = models.ManyToManyField(Service, blank=True)
    addedOn = models.DateTimeField(auto_now_add=True)
    updatedOn = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"

    def __str__(self) -> str:
        return f"{self.name}"
