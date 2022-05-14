"""success URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('sign/', include('sign.urls')),
    path('admin_equipment/', include('admin_equipment.urls')),
    path('admin_equipment_detail/', include('admin_equipment_detail.urls')),
    path('admin_equipment_history/', include('admin_equipment_history.urls')),
    path('admin_equipment_manage/', include('admin_equipment_manage.urls')),
    path('admin_main/', include('admin_main.urls')),
    path('user_equipment/', include('user_equipment.urls')),
    path('user_history/', include('user_history.urls')),
    path('user_main/', include('user_main.urls')),
    path('user_mypage/', include('user_mypage.urls')),
    path('user_rental/', include('user_rental.urls'))
]
