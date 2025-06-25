from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.http import JsonResponse 

# ✅ Tambahkan fungsi ini
def home(request):
    return JsonResponse({"message": "Pomodoro API is running."})

urlpatterns = [
    path('', home),  
    path('admin/', admin.site.urls),
    path('api/', include('pomodoro_api.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
