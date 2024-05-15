import re
from django.shortcuts import render, get_object_or_404
from .models import SubnetGen
from .forms import SubnetSelectForm
from .forms import SubnetGenForm
from django.contrib import messages
from .models import Device
from .forms import DeviceForm


def subnet_details_view(request):
    subnet_id = request.GET.get('subnet_select')
    subnet = get_object_or_404(SubnetGen, id=subnet_id)
    devices = Device.objects.filter(subnets__id=subnet_id)
    context = subnet.NetworkAdress()
    context['devices'] = devices
    return render(request, 'details/index.html', context)

def subnet_view(request):
    form = SubnetSelectForm()
    return render(request, 'subnets/index.html', {'form': form})

def subnet_create_view(request):
    if request.method == 'POST':
        form = SubnetGenForm(request.POST)
        print(form)
        if form.is_valid():
            subnet = form.cleaned_data.get('IpAdresswithCDIR')  
            if not re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\/\d{1,2}$', subnet):
                messages.error(request, 'Invalid subnet. Please enter a subnet in the format xxx.xxx.xxx.xxx/xx')
            else:
                if SubnetGen.objects.filter(IpAdresswithCDIR=subnet).exists():
                    messages.error(request, 'This subnet already exists.')
                else:
                    form.save()
                    messages.success(request, 'Subnet created successfully.')
    else:
        form = SubnetGenForm()
    return render(request, 'create/index.html', {'form': form})

def home_view(request):
    return render(request, 'home/index.html')

def device_create_view(request):
    if request.method == 'POST':
        form = DeviceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Device created successfully.')
            
    else:
        form = DeviceForm()
    return render(request, 'devicecreate/index.html', {'form': form})

def device_list_view(request):
    devices = Device.objects.all()
    return render(request, 'devices/index.html', {'devices': devices})