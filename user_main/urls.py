from django.urls import path
from . import views
#

urlpatterns = [
    path('user_main/', views.user_main),
]