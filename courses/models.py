from django.db import models

from agency.models import Agency

# Create your models here.

# A course is a designated area for certain classes
# A course has a course date
# Course names are designated at the agency level?


class Course(models.Model):
    name = models.CharField(max_length=200, null=True)
    addedOn = models.DateTimeField(auto_now_add=True)
    updatedOn = models.DateTimeField(auto_now=True)
    courseDate = models.DateField(db_index=True)
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"

    def __str__(self) -> str:
        return f"{self.name}"


# A course can have many courseClasses per the foreignKey assignment
# A class can have many clients tied to each class, shows this relationship on the customer table
# needs a classmethod to get_all_class_customers
class CourseClass(models.Model):
    name = models.CharField(max_length=200, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    addedOn = models.DateTimeField(auto_now_add=True)
    updatedOn = models.DateTimeField(auto_now=True)
    classDate = models.DateField(db_index=True)

    class Meta:
        verbose_name = "Class"
        verbose_name_plural = "Classes"

    def __str__(self) -> str:
        return f"{self.name}"
