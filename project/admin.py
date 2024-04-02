from django.contrib import admin
from .models import *

class Project_admin(admin.ModelAdmin):
    list_display = ['id', 'name', 'yard', 'owner', '_class', 'pm']

class Element_admin(admin.ModelAdmin):
    list_display = ['marking', 'mark', 'discipline', 'block', 'zone', 'deck', 'project', 'status']


admin.site.register(Project, Project_admin)
admin.site.register(Element, Element_admin)
admin.site.register(Discipline)
admin.site.register(ProjectType)
