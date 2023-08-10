from django.test import TestCase
from datetime import date
from .models import Course, CourseClass
from agency.models import Agency  # Adjust import based on your project structure
# Adjust import based on your project structure
from customers.models import Customer


class CourseClassModelTestCase(TestCase):
    def setUp(self):
        # Create a sample agency and course
        self.agency = Agency.objects.create(name="Sample Agency")
        self.course = Course.objects.create(
            name="Test Course",
            courseDate=date.today(),
            agency=self.agency
        )

    def test_course_class_creation(self):
        course_class = CourseClass.objects.create(
            name="Test Class",
            course=self.course,
            classDate=date.today()
        )
        self.assertEqual(course_class.__str__(), "Test Class")

    # Add more test cases as needed

# Add more test classes and test cases as needed
