from django.contrib import admin
from .models import *
from django import forms
from .forms import RemarkAdminForm

class CCOS_admin(admin.ModelAdmin):
    list_display = ['id', 'project', 'creation_date', 'discipline']
    
class Remark_admin(admin.ModelAdmin):
    list_display = ['id', 'element', 'open']
    form = RemarkAdminForm
    
admin.site.register(CCOS, CCOS_admin)
admin.site.register(Remark, Remark_admin)