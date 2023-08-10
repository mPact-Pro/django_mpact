from django.db import models
from dateutil.relativedelta import relativedelta
from datetime import date, timedelta
from django.db.models import Q

# Define a custom manager for the Session model


class SessionManager(models.Manager):
    # Method to retrieve sessions associated with a specific customer
    def sessions_for_customer(self, customer):
        return self.filter(customer=customer)


class Session(models.Model):
    name = models.CharField(max_length=200, null=True)
    addedOn = models.DateTimeField(auto_now_add=True)
    updatedOn = models.DateTimeField(auto_now=True)
    sessionDate = models.DateField(db_index=True)
    agency = models.ForeignKey(
        'agency.Agency', on_delete=models.CASCADE, default='1')

    class Meta:
        verbose_name = "Session"
        verbose_name_plural = "Sessions"

    # Attach the custom manager to the model
    objects = SessionManager()

    # Private method to filter sessions based on a date range
    @classmethod
    def _filter_by_date_range(cls, start_date, end_date):
        return cls.objects.filter(sessionDate__range=(start_date, end_date)).distinct()

    # Method to retrieve sessions within the current fiscal year
    @classmethod
    def get_sessions_current_fiscal_year(cls):
        # Calculate the start and end dates of the current fiscal year
        today = date.today()
        fiscal_year_start = date(today.year, 10, 1)
        fiscal_year_end = date(today.year + 1, 9, 30)

        # Call the private method to filter sessions by date range
        return cls._filter_by_date_range(fiscal_year_start, fiscal_year_end)

    # Method to retrieve sessions within the current quarter
    @classmethod
    def get_sessions_current_quarter(cls):
        today = date.today()
        current_year = today.year
        current_month = today.month

        quarters = [(1, 3), (4, 6), (7, 9), (10, 12)]

        # Determine the start and end months of the current quarter
        for start_month, end_month in quarters:
            if start_month <= current_month <= end_month:
                quarter_start = date(current_year, start_month, 1)
                quarter_end = date(current_year, end_month, 1) + \
                    relativedelta(months=1) - timedelta(days=1)
                # Call the private method to filter sessions by date range
                return cls._filter_by_date_range(quarter_start, quarter_end)

    # Method to provide a human-readable representation of the session
    def __str__(self) -> str:
        return f"{self.name}"


class SessionOutcome(models.Model):
    name: models.CharField(max_length=200, null=True)
    outcome: models.CharField(max_length=25)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "SessionOutcome"
        verbose_name_plural = "SessionOutcomes"

    def __str__(self) -> str:
        return f"{self.name}"
