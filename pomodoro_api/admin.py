from django.contrib import admin
from .models import PomodoroSession, Motivasi  

# Daftarkan model
admin.site.register(PomodoroSession)
admin.site.register(Motivasi)
