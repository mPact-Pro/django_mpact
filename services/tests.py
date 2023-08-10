from django.test import TestCase
from datetime import date
from .models import Service
from agency.models import Agency  # Adjust import based on your project structure


class ServiceModelTestCase(TestCase):
    def setUp(self):
        # Create a sample agency
        self.agency = Agency.objects.create(name="Sample Agency")

    def test_service_creation(self):
        service = Service.objects.create(
            name="Test Service",
            serviceDate=date.today(),
            agency=self.agency
        )
        self.assertEqual(service.__str__(), "Test Service")

    # Add more test cases as needed

# Add more test classes and test cases as needed
