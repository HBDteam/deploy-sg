from django.shortcuts import render, redirect
from .models import Equip, EquipCode
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def EquipModify(request):
    equipid = request.GET.get('equipid')
    equip_infos = Equip.objects.filter(equipID=equipid)
    categories = EquipCode.objects.all()
    context = {'equip_infos': equip_infos, 'categories': categories}
    return render(request, 'admin_equipment_manage.html', context)


@csrf_exempt
def Modify(request):
    equipid = request.POST['equipID']
    equips = Equip.objects.filter(equipID=equipid)
    for equip in equips:
        if request.POST.get('equipCode') is None:
            equip.equipID = request.POST['equipID']
            equip.receivedDate = request.POST['receivedDate']
            equip.isRented = request.POST['isRented']
            equip.status = request.POST['status']
            equip.equipInfo = request.POST['equipInfo']
            equip.save()
        else:
            equip.equipCode = request.POST['equipCode']
            equip.equipID = request.POST['equipID']
            equip.receivedDate = request.POST['receivedDate']
            equip.isRented = request.POST['isRented']
            equip.status = request.POST['status']
            equip.equipInfo = request.POST['equipInfo']
            equip.save()
    return redirect('http://127.0.0.1:8000/admin_equipment_detail/', {'alert': '수정되었습니다'})
