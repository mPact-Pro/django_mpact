from django.test import TestCase
from datetime import date
from .models import Session, SessionOutcome
from agency.models import Agency


class SessionModelTestCase(TestCase):
    def setUp(self):
        # Create a sample agency
        self.agency = Agency.objects.create(name="Sample Agency")

    def test_session_creation(self):
        session = Session.objects.create(
            name="Test Session",
            sessionDate=date.today(),
            agency=self.agency
        )
        self.assertEqual(session.__str__(), "Test Session")

    def test_get_sessions_current_fiscal_year(self):
        # Create a session within the current fiscal year
        Session.objects.create(
            name="Session in Current Fiscal Year",
            sessionDate=date.today(),
            agency=self.agency
        )

        sessions = Session.get_sessions_current_fiscal_year()
        self.assertEqual(sessions.count(), 1)

    # Add more test cases as needed


class SessionOutcomeModelTestCase(TestCase):
    def setUp(self):
        # Create a sample agency and session
        self.agency = Agency.objects.create(name="Sample Agency")
        self.session = Session.objects.create(
            name="Test Session",
            sessionDate=date.today(),
            agency=self.agency
        )

    def test_session_outcome_creation(self):
        outcome = SessionOutcome.objects.create(
            name="Test Outcome",
            outcome="Success",
            session=self.session
        )
        self.assertEqual(outcome.__str__(), "Test Outcome")

    # Add more test cases as needed

# Add more test classes and test cases as needed
