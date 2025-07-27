from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PomodoroSessionViewSet,MotivasiViewSet,RegisterView,TimeEntryView,AdminTimeEntryView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


#
router = DefaultRouter()
router.register(r'sessions', PomodoroSessionViewSet)
router.register(r'motivasi', MotivasiViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),  
    path('time-entry/', TimeEntryView.as_view(), name='time-entry'),

    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/time-entries/', AdminTimeEntryView.as_view(), name='admin-time-entries'),
]
