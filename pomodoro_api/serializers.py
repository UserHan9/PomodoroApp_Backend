from rest_framework import serializers
from .models import TimeEntry, PomodoroSession, Motivasi
from django.utils import timezone
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
    user = serializers.StringRelatedField()
    relative_created_at = serializers.SerializerMethodField()

    class Meta:
        model = TimeEntry
        fields = ['id', 'duration','relative_created_at', 'user']
        read_only_fields = ['user']

    def get_relative_created_at(self, obj):
        now = timezone.now()
        diff = now - obj.created_at

        if diff.days == 0:
            return "Today"
        elif diff.days == 1:
            return "Yesterday"
        elif diff.days < 7:
            return f"{diff.days} days ago"
        elif diff.days < 30:
            weeks = diff.days // 7
            return f"{weeks} week{'s' if weeks > 1 else ''} ago"
        elif diff.days < 365:
            months = diff.days // 30
            return f"{months} month{'s' if months > 1 else ''} ago"
        else:
            years = diff.days // 365
            return f"{years} year{'s' if years > 1 else ''} ago"


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