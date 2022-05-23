from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    
    path('', views.aichatbot),
    path('aiAnswer/', views.aiAnswer_ajax)
]