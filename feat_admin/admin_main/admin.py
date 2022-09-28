from django.contrib import admin
from .models import Equip, EquipCode
from feat_user.user_main.models import Renting, Lab
from sign.models import User, Manager


admin.site.register(EquipCode)
admin.site.register(Equip)
admin.site.register(Renting)
admin.site.register(Lab)
admin.site.register(User)
admin.site.register(Manager)
