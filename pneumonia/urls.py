
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('prediction.urls')),
    # path('admin/', admin.site.urls),
   path('admin/', admin.site.urls, name='admin'),
  ]
