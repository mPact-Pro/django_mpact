from django.db import models
from django.db.models import Q
from datetime import date

from agency.models import Agency

# Create your models here.

# Sessions are the bread and butter of mPact
# A customer can have many sessions, and a session can have many outcomes
# Reporting is based around the sessionDate
# should be able to return or potentially partition sessions based on FY for reporting purposes


class Session(models.Model):
    name = models.CharField(max_length=200, null=True)
    addedOn = models.DateTimeField(auto_now_add=True)
    updatedOn = models.DateTimeField(auto_now=True)
    sessionDate = models.DateField(db_index=True)
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Session"
        verbose_name_plural = "Sessions"

    def __str__(self) -> str:
        return f"{self.name}"

    @classmethod
    def get_sessions_current_fiscal_year(cls):
        # Determine the start and end dates of the current fiscal year (Oct 1 to Sept 30)
        today = date.today()
        fiscal_year_start = date(today.year, 10, 1)
        fiscal_year_end = date(today.year + 1, 9, 30)

        # Filter sessions within the current fiscal year
        # Q translates to native SQL query, this is querying the data in realtime
        # sql so it "should" be fast since the sessions will be limited by agency
        # for the query
        sessions = cls.objects.filter(
            Q(sessionDate__gte=fiscal_year_start) & Q(
                sessionDate__lte=fiscal_year_end)
        ).distinct()

        return sessions


class SessionOutcome(models.Model):
    name: models.CharField(max_length=200, null=True)
    outcome: models.CharField(max_length=25)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "SessionOutcome"
        verbose_name_plural = "SessionOutcomes"

    def __str__(self) -> str:
        return f"{self.name}"
