from django.db import models
from django.contrib.auth.models import User

class PomodoroSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    success = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {'Success' if self.success else 'Failed'}"
