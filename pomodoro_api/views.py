from rest_framework import viewsets
from .models import PomodoroSession,Motivasi
from .serializers import PomodoroSessionSerializer,MotivasiSerializer

class PomodoroSessionViewSet(viewsets.ModelViewSet):
    queryset = PomodoroSession.objects.all()
    serializer_class = PomodoroSessionSerializer

class MotivasiViewSet(viewsets.ModelViewSet):
    queryset = Motivasi.objects.all().order_by('-tanggal_dibuat')
    serializer_class = MotivasiSerializer