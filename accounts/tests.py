from django.test import TestCase
from .models import User
from agency.models import Agency


class UserModelTestCase(TestCase):
    def setUp(self):
        # Create a sample agency
        self.agency = Agency.objects.create(name="Sample Agency")

    def test_user_creation(self):
        user = User.objects.create(
            username="testuser",
            agency=self.agency,
            role="admin"
        )
        self.assertEqual(user.__str__(), "testuser")

    # Add more test cases as needed

# Add more test classes and test cases as needed
