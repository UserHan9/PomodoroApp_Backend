from ast import List
from email.policy import HTTP
from urllib import response
from rest_framework.permissions import IsAdminUser
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from .models import PomodoroSession,Motivasi, TimeEntry
from .serializers import PomodoroSessionSerializer,MotivasiSerializer,TimeEntrySerializer,RegisterSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated


##SESSION VIEW
class PomodoroSessionViewSet(viewsets.ModelViewSet):
    queryset = PomodoroSession.objects.all()
    serializer_class = PomodoroSessionSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

##MOTIVATION VIEW
class MotivasiViewSet(viewsets.ModelViewSet):
    queryset = Motivasi.objects.all().order_by('-tanggal_dibuat')
    serializer_class = MotivasiSerializer

##REGISTER VIEW
class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

##TIMEENTRY VIEW
class TimeEntryView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = TimeEntrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)  # user token
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        entries = TimeEntry.objects.filter(user=request.user)
        serializer = TimeEntrySerializer(entries, many=True)
        return Response(serializer.data)

class TimeEntryPagination(PageNumberPagination):
    page_size = 5  
    page_size_query_param = 'page_size'
    max_page_size = 100

##TIMEENTRY ATMIN ONLY
class AdminTimeEntryView(ListAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = TimeEntrySerializer
    queryset = TimeEntry.objects.all().order_by('-created_at')
    pagination_class = TimeEntryPagination