from django.db import models

from mPactSessions.models import Session


# Base Agency table, Every user will be assigned an agency
# Each customer will only be available to that agency
# Each customers sessions, services, or courses will only
# be available to that users agency
# Basis of multi-tenency for the frontend application
# User data gets stored in session cookie or token for queries
class Agency(models.Model):
    name = models.CharField(max_length=200, null=True)

    class Meta:
        verbose_name = "Agency"
        verbose_name_plural = "Agencies"

    def __str__(self) -> str:
        return f"{self.name}"

    # Logged in User will have an agency id stored in the users session token or cookie,
    # Along with other needed data. ID stored in the cookie will be used to properly
    # fetch the current agency data to provide to the logged in counselor or admin
    def get_all_users(self):
        # Retrieve all agency users counselors and admins
        return self.user_set.all()

    def get_all_customers(self):
        # Retrieve all customers associated with this agency
        return self.customer_set.all()

    def get_all_courses(self):
        # Retrieve all courses associated with this agency
        return self.course_set.all()

    def get_all_services(self):
        # Retrieves all services associated with this agency
        return self.service_set.all()

    def get_all_sessions(self):
        # Retrieves all sessions associated with this agency
        return self.session_set.all()

    def get_sessions_current_fiscal_year(self):
        # Uses the class method on sessions to return current FY sessions tied to this agency
        return Session.get_sessions_current_fiscal_year().filter(agency=self)

    def get_sessions_current_fiscal_quarter(self):
        # Uses the class method on sessions to return current FY quarter sessions tied to this agency
        return Session.get_sessions_current_quarter().filter(agency=self)
