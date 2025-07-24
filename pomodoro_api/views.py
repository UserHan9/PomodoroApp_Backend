from email.policy import HTTP
from urllib import response
from rest_framework import viewsets
from .models import PomodoroSession,Motivasi, TimeEntry
from .serializers import PomodoroSessionSerializer,MotivasiSerializer,TimeEntrySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated




class PomodoroSessionViewSet(viewsets.ModelViewSet):
    queryset = PomodoroSession.objects.all()
    serializer_class = PomodoroSessionSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class MotivasiViewSet(viewsets.ModelViewSet):
    queryset = Motivasi.objects.all().order_by('-tanggal_dibuat')
    serializer_class = MotivasiSerializer

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        if User.objects.filter(username=username).exists():
            return Response({"error": "Username sudah digunakan"}, status=status.HTTP_400_BAD_REQUEST)
        
        user = User.objects.create_user(username=username, email=email, password=password)
        refresh = RefreshToken.for_user(user)
        

        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_201_CREATED)

class TimeEntryView(APIView):
    permission_classes = [AllowAny]  # Allow access without authentication

    def post(self, request):
        serializer = TimeEntrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        entries = TimeEntry.objects.all()  # Return all entries since no user info
        serializer = TimeEntrySerializer(entries, many=True)
        return Response(serializer.data)