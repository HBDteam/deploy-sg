from django.urls import path
from . import views

urlpatterns = [
    path('', views.adminMain),
    path('admin_renting/', views.renting),
    path('rent_detail_ajax/', views.rent_detail_ajax),
    path('admin_returning/', views.returning),
    path('return_detail_ajax/', views.return_detail_ajax)
]
