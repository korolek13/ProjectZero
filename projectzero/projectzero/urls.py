from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('homepage.urls')),
    path('icecream/', include('icecream.urls')),
    path('admin/', admin.site.urls),
]
