from django.contrib import admin

from .models import Device, SubnetGen

# Add Both to Admin
admin.site.register(SubnetGen)
admin.site.register(Device)