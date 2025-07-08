from rest_framework import serializers
from .models import PomodoroSession
from .models import Motivasi

class PomodoroSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PomodoroSession
        fields = '__all__'

class MotivasiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motivasi
        fields = '__all__'