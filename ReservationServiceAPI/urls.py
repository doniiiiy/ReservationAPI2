
from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('ReservationApp.urls')),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/', include('djoser.urls')),
    re_path(r'^auth', include('djoser.urls.authtoken')),
]
