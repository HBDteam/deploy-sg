from django.urls import path
from . import views
#

urlpatterns = [
    path('rental/', views.rental),
]