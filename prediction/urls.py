from django.urls import path
from django.contrib import admin
from . import views
urlpatterns = [
    path("",views.index, name='index'),    
    path("my_view",views.my_view, name='my_view'),
    # path('admin/', admin.site.urls, name='admin'),
    path('about/', views.about, name='about'),
]