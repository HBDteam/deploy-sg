from django.shortcuts import render, redirect
from .models import Equip, EquipCode
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


@csrf_exempt
def EquipRegister(request):
    if request.method == 'GET':
        categories = EquipCode.objects.all()
        context = {'categories': categories}
        return render(request, 'admin_equipment.html', context)
    elif request.method == 'POST':
        equipcode = request.POST['equipCode']
        equipID = request.POST['equipID']
        receivedDate = request.POST['receivedDate']
        isRented = request.POST['isRented']
        status = request.POST['status']
        equipInfo = request.POST['equipInfo']
        newEquip = Equip.objects.create(equipCode=EquipCode.objects.get(equipCode=equipcode), equipID=equipID,
                                        receivedDate=receivedDate, isRented=isRented, status=status, equipInfo=equipInfo)
        return redirect('http://www.sunggongee.shop/feat_admin/admin_equipment_detail/', {'alert': '수정되었습니다'})
