from django.db import models

from customers.models import Customer

# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=200, null=True)

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    def __str__(self) -> str:
        return f'{self.name}'


class CourseClass(models.Model):
    name = models.CharField(max_length=200, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    customers = models.ManyToManyField(Customer, blank=True)

    class Meta:
        verbose_name = 'Class'
        verbose_name_plural = 'Classes'

    def __str__(self) -> str:
        return f'{self.name}'
