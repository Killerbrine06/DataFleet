from django.contrib import admin
from .models import *

class CCC_admin(admin.ModelAdmin):
    list_display = ['id', 'name', 'year', 'director']
    
class Person_admin(admin.ModelAdmin):
    list_display = ['id', 'name', 'employer', 'phone']
    

admin.site.register(CCC, CCC_admin)
admin.site.register(Facility)
admin.site.register(Person, Person_admin)