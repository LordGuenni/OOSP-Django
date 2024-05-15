from django.db import models
import ipaddress

class SubnetGen(models.Model):
    IpAdresswithCDIR = models.CharField(max_length=18)
    
    def __str__(self):
        return self.IpAdresswithCDIR

    def NetworkAdress(self):
        ip_addr = ipaddress.ip_interface(self.IpAdresswithCDIR)
        net_addr = ip_addr.network
        pref_len = ip_addr.with_prefixlen
        mask = ip_addr.with_netmask
        wildcard = ip_addr.hostmask
        broadcast_address = net_addr.broadcast_address
        context = {
            'network_address': str(net_addr).split('/')[0],
            'broadcast_address': broadcast_address,
            'cidr_notation': pref_len.split('/')[1],
            'subnet_mask': mask.split('/')[1],
            'wildcard_mask': wildcard,
            'first_ip': list(net_addr.hosts())[0],
            'last_ip': list(net_addr.hosts())[-1],
        }
        return context 

class Device(models.Model):
    DEVICE_TYPES = [
        ('MOBILE', 'Mobile'),
        ('DESKTOP', 'Desktop'),
    ]

    name = models.CharField(max_length=100)
    device_type = models.CharField(max_length=7, choices=DEVICE_TYPES, default='DESKTOP')
    subnets = models.ManyToManyField(SubnetGen)

    def __str__(self):
        return self.name