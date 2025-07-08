from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PomodoroSessionViewSet,MotivasiViewSet,RegisterView

#
router = DefaultRouter()
router.register(r'sessions', PomodoroSessionViewSet)
router.register(r'motivasi', MotivasiViewSet)

urlpatterns = [
    path('', include(router.urls)),
     path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),  
]
