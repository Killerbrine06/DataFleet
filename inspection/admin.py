from django.contrib import admin
from .models import *
from django import forms
from .forms import RemarkAdminForm

class CCOS_admin(admin.ModelAdmin):
    list_display = ['id', 'project', 'creation_date', 'discipline']
    
class Remark_admin(admin.ModelAdmin):
    list_display = ['id', 'element', 'open', 'created_by_full_name']
    form = RemarkAdminForm
    
    def created_by_full_name(self, obj:Remark) -> str:
        return obj.created_by.first_name + ' ' + obj.created_by.last_name
    
admin.site.register(CCOS, CCOS_admin)
admin.site.register(Remark, Remark_admin)