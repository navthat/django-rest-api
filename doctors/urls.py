#doctors/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('doctors/', include('api.urls')),
    path('admin/', admin.site.urls),
]