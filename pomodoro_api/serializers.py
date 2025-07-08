from rest_framework import serializers
from .models import PomodoroSession
from .models import Motivasi

class PomodoroSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PomodoroSession
        fields = ['id', 'start_time', 'end_time', 'success']

class MotivasiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motivasi
        fields = ['id','teks','pembuat']