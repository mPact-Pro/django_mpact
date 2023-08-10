from django.contrib import admin

from mPactSessions.models import Session, SessionOutcome

# Register your models here.
admin.site.register(Session)
admin.site.register(SessionOutcome)
