


from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views as drf_views
from django.http import HttpResponse

urlpatterns = [
    path('', lambda request: HttpResponse("Welcome to the Django Client-Project API")),
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),
    path('api/token/', drf_views.obtain_auth_token),  # ✅ This is the important line
]
