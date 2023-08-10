from django.test import TestCase
from .models import Agency
from accounts.models import User
from customers.models import Customer
from courses.models import Course
from mPactSessions.models import Session
from services.models import Service


class AgencyModelTestCase(TestCase):
    def setUp(self):
        # Create a sample agency
        self.agency = Agency.objects.create(name="Sample Agency")

    def test_get_all_users(self):
        # Create sample users associated with the agency
        user1 = User.objects.create(username="user1", agency=self.agency)
        user2 = User.objects.create(username="user2", agency=self.agency)

        users = self.agency.get_all_users()
        self.assertEqual(users.count(), 2)

    def test_get_all_customers(self):
        # Create sample customers associated with the agency
        customer1 = Customer.objects.create(
            name="Customer 1", agency=self.agency)
        customer2 = Customer.objects.create(
            name="Customer 2", agency=self.agency)

        customers = self.agency.get_all_customers()
        self.assertEqual(customers.count(), 2)

    # Similar tests for get_all_courses, get_all_services, and get_all_sessions

    # Add more test cases as needed

# Add more test classes and test cases as needed
