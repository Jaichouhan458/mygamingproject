from django.contrib import admin
from .models import Data,User_Info

class DataModelAdmin(admin.ModelAdmin):
    
    list_display = ('name', 'lastname', 'email', 'message', 'subject')
    
admin.site.register(Data,DataModelAdmin)

class User_InfoModelAdmin(admin.ModelAdmin):
    
    list_display = ('fullname', 'username', 'email', 'Password')

admin.site.register(User_Info,User_InfoModelAdmin)
    