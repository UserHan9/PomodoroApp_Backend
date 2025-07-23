from django.db import models
from django.contrib.auth.models import User

class PomodoroSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    success = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {'Success' if self.success else 'Failed'}"

##QUOTE DATABASE MODEL
class Motivasi(models.Model):
    teks = models.TextField()
    pembuat = models.CharField(max_length=100, blank=True)
    tanggal_dibuat = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.teks[:50]


##TIME ENTRY DATABASE MODEL
class TimeEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='time_entries')
    duration = models.IntegerField(help_text="Duration in seconds")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.duration}s at {self.created_at}"