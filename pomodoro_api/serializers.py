from rest_framework import serializers
from .models import PomodoroSession
from .models import Motivasi
from .models import TimeEntry
from django.contrib.auth.models import User

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
        fields = ['id', 'duration', 'created_at']

##REGISTER SERIALIZER
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )
        return user