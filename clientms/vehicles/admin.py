from django.contrib import admin

from .models import VehicleInformation

class VehicleAdmin(admin.ModelAdmin):
    model = VehicleInformation
    
class VehicleInLine(admin.TabularInline):
    model = VehicleInformation
    
admin.site.register(VehicleInformation, VehicleAdmin)
