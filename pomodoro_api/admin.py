from django.contrib import admin
from .models import PomodoroSession, Motivasi, TimeEntry

# Daftarkan model
admin.site.register(PomodoroSession)
admin.site.register(Motivasi)
admin.site.register(TimeEntry)
