from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('send_email/', include('send_email.urls')),
    path('admin/', admin.site.urls),
]

