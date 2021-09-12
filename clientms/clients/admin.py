from django.contrib import admin

from .models import Client, Comment
from vehicles.admin import VehicleInLine

class CommentInLine(admin.TabularInline):
    model = Comment
     
class ClientAdmin(admin.ModelAdmin):
    inlines = [
        CommentInLine,
        VehicleInLine,
    ]
    
admin.site.register(Client, ClientAdmin)
admin.site.register(Comment)