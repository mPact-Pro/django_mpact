from datetime import date
from django.test import TestCase
from .models import Customer
from agency.models import Agency
from courses.models import CourseClass, Course
from mPactSessions.models import Session
from services.models import Service


class CustomerModelTestCase(TestCase):
    def setUp(self):
        self.agency = Agency.objects.create(name="Sample Agency")
        self.session = Session.objects.create(
            name="Sample Session", agency=self.agency)
        self.course = Course.objects.create(
            name="Test Course",
            courseDate=date.today(),
            agency=self.agency
        )

    def test_get_all_sessions(self):
        customer = Customer.objects.create(
            name="Test Customer",
            email="test@example.com",
            agency=self.agency,
            sessions=self.session
        )

        sessions = customer.get_all_sessions()
        self.assertEqual(sessions.count(), 1)

    def test_get_all_services(self):
        # Create a sample service associated with the customer
        service = Service.objects.create(
            name="Sample Service", agency=self.agency)
        customer = Customer.objects.create(
            name="Test Customer",
            email="test@example.com",
            agency=self.agency
        )
        customer.services.add(service)

        services = customer.get_all_services()
        self.assertEqual(services.count(), 1)

    def test_get_all_classes(self):
        # Create a sample course class associated with the customer
        course_class = CourseClass.objects.create(
            name="Sample Class", course=self.course, classDate=date.today())
        customer = Customer.objects.create(
            name="Test Customer",
            email="test@example.com",
            agency=self.agency
        )
        customer.courseClass.add(course_class)

        classes = customer.get_all_classes()
        self.assertEqual(classes.count(), 1)

# Add more test classes and test cases as needed
