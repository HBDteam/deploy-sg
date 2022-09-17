from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('sign/', include('sign.urls')),
    path('admin_main/', include('admin_main.urls')),
    path('user_main/',include('user_main.urls'))
]
