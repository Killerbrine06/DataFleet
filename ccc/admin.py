from django.contrib import admin
from .models import *

class CCC_admin(admin.ModelAdmin):
    list_display = ['id', 'name', 'year', 'director_fullname', 'type']
    
    def director_fullname(self, obj:CCC) -> str:
        return obj.director.first_name + ' ' + obj.director.last_name
    
class Person_admin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'employer', 'phone']
    
    def full_name(self, obj:Person) -> str:
        return obj._user.first_name + " " + obj._user.last_name
    

admin.site.register(CCC, CCC_admin)
admin.site.register(Facility)
admin.site.register(Person, Person_admin)