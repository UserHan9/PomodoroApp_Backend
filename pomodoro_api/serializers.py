from rest_framework import serializers
from .models import PomodoroSession
from .models import Motivasi
from .models import TimeEntry

class PomodoroSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PomodoroSession
        fields = ['id', 'start_time', 'end_time', 'success']

##MOTIVATION SERIALIZER
class MotivasiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motivasi
        fields = ['id','teks','pembuat']

##TIME ENTRY SERIALIZER
class TimeEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeEntry
        fields = ['id', 'duration', 'activity', 'created_at']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)