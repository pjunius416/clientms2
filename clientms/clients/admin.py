from django.contrib import admin

from .models import Client, Comment

class ClientAdmin(admin.ModelAdmin):
    model = Client
    
class CommentInLine(admin.TabularInline):
    model = Comment
    
class ClientAdmin(admin.ModelAdmin):
    inlines = [
        CommentInLine,
    ]
    
admin.site.register(Client, ClientAdmin)
admin.site.register(Comment)