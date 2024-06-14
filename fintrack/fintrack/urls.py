from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('api/', include('api.urls')),
    path('api/auth/', include('dj_rest_auth.urls')),
]