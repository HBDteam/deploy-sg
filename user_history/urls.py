from django.urls import path
from . import views
#

urlpatterns = [
    path('user_history/', views.user_history),
]