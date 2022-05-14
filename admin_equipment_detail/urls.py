from django.urls import path
from . import views

urlpatterns = [
    path('admin_equipment_detail/', views.adminEquipDetail)
]
