from django.urls import path
from . import views

urlpatterns = [
    path('sign/', views.sign),
    path('signup/', views.signup),
    path('signin/', views.signin),
]