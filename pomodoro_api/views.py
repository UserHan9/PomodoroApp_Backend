from rest_framework import viewsets
from .models import PomodoroSession
from .serializers import PomodoroSessionSerializer

class PomodoroSessionViewSet(viewsets.ModelViewSet):
    queryset = PomodoroSession.objects.all()
    serializer_class = PomodoroSessionSerializer
