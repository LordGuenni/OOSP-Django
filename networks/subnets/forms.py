from django import forms
from .models import SubnetGen
from .models import Device

class IPAddressForm(forms.Form):
    IpAdresswithCDIR = forms.CharField(label='Geben Sie die IP-Adresse im IP/Masken-Format ein:', max_length=100)
    
class SubnetSelectForm(forms.Form):
    subnet_select = forms.ModelChoiceField(queryset=SubnetGen.objects.all())
    
class SubnetGenForm(forms.ModelForm):
    class Meta:
        model = SubnetGen
        fields = '__all__'  

class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ['name', 'device_type', 'subnets']