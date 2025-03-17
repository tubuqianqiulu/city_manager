"""
URL configuration for city_manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import HostListCreateView, HostRetrieveUpdateDestroyView, PingHostView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hosts/', HostListCreateView.as_view(), name='host-list-create'),
    path('hosts/<int:pk>/', HostRetrieveUpdateDestroyView.as_view(), name='host-retrieve-update-destroy'),
    path('hosts/<int:pk>/ping/', PingHostView.as_view(), name='host-ping'),
]
