from django.contrib import admin
from .models import Data

class DataModelAdmin(admin.ModelAdmin):
    
    list_display = ('name', 'lastname', 'email', 'message', 'subject')
    
admin.site.register(Data,DataModelAdmin)