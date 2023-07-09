from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('home.urls')),
]

urlpatterns += static(settings.STATIC_URL, dokuments_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, dokuments_root=settings.MEDIA_ROOT)