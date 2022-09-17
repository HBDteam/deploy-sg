from django.urls import path
from . import views

urlpatterns = [
    path('', views.EquipModify),
    path('modify/', views.Modify)
]
