from django.urls import path
from . import views
#

urlpatterns = [
    path('user_mypage/', views.user_mypage),
]