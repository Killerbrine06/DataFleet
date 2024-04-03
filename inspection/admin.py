from django.contrib import admin
from .models import *

class CCOS_admin(admin.ModelAdmin):
    list_display = ['id', 'project', 'creation_date', 'discipline']
    
class Remark_admin(admin.ModelAdmin):
    list_display = ['id', 'element', 'open']
    
admin.site.register(CCOS, CCOS_admin)
admin.site.register(Remark, Remark_admin)