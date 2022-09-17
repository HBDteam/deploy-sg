from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('sign/', include('sign.urls')),
    path('feat_admin/admin_main/', include('feat_admin.admin_main.urls')),
    path('feat_user/user_main/',include('feat_user.user_main.urls'))
]
