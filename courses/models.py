from django.db import models
from django.db.models import Q
from datetime import date
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
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE, default='1')

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

    def get_customers(self):
        # Get all customers associated with this CourseClass
        return self.customers.all()

    @classmethod
    def get_classes_current_fiscal_year(cls):
        # Determine the start and end dates of the current fiscal year (Oct 1 to Sept 30)
        today = date.today()
        fiscal_year_start = date(today.year - 1, 10, 1)
        fiscal_year_end = date(today.year + 1, 9, 30)

        # Filter classes within the current fiscal year
        # Q translates to native SQL query, this is querying the data in realtime
        # sql so it "should" be fast since the classes will be limited by agency
        # for the query
        classes = cls.objects.filter(
            Q(classDate__gte=fiscal_year_start) & Q(
                classDate__lte=fiscal_year_end)
        ).distinct()

        return classes
