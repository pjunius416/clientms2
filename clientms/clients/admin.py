from django.contrib import admin

from .models import Client, Comment, VehicleInformation

class CommentInLine(admin.TabularInline):
    model = Comment
    
class VehicleInLine(admin.TabularInline):
    model = VehicleInformation
    
class ClientAdmin(admin.ModelAdmin):
    inlines = [
        CommentInLine,
        VehicleInLine,
    ]
    
admin.site.register(Client, ClientAdmin)
admin.site.register(Comment)
admin.site.register(VehicleInformation)