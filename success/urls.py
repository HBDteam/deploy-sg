from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('sign/', include('sign.urls')),
    path('aichatbot/', include('aichatbot.urls')),
    path('feat_admin/admin_main/', include('feat_admin.admin_main.urls')),
    path('feat_user/user_main/',include('feat_user.user_main.urls')),
    path('feat_user/user_equipment/',include('feat_user.user_equipment.urls')),
    path('feat_user/user_history/',include('feat_user.user_history.urls')),
    path('feat_user/user_mypage/',include('feat_user.user_mypage.urls')),
    path('feat_user/user_rental/',include('feat_user.user_rental.urls')),
    path('feat_admin/admin_equipment/', include('feat_admin.admin_equipment.urls')),
    path('feat_admin/admin_equipment_manage/', include('feat_admin.admin_equipment_manage.urls')),
    path('feat_admin/admin_equipment_detail/', include('feat_admin.admin_equipment_detail.urls')),
    path('feat_admin/admin_equipment_history/', include('feat_admin.admin_equipment_history.urls')),
    path('feat_user/user_main/', include('feat_user.user_main.urls')),
    path('feat_user/user_equipment/', include('feat_user.user_equipment.urls')),
    path('feat_user/user_history/', include('feat_user.user_history.urls')),
    path('feat_user/user_rental/', include('feat_user.user_rental.urls'))
]
