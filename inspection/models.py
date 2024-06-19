import datetime
from django.db import models
from ccc.models import Person
from project.models import Project, Element, Discipline

class Remark(models.Model):
    element = models.ForeignKey(Element, on_delete=models.CASCADE)
    inspection = models.ForeignKey('CCOS', on_delete=models.CASCADE)
    open = models.BooleanField(default=True)
    
    def __str__(self):
        return f'{self.inspection.id}-{self.id}'

class CCOS(models.Model):
    class Meta:
        verbose_name = 'CCOS'
        verbose_name_plural = 'CCOSs'
        
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    
    creation_date = models.DateField(default=datetime.date.today)
    class_inspection_date = models.DateField(null=True)
    class_inspection_date_closed = models.DateField(null=True)
    owner_inspection_date = models.DateField(null=True)
    owner_inspection_date_closed = models.DateField(null=True)
    
    discipline = models.ForeignKey(Discipline, null=True, on_delete=models.SET_NULL)
    description = models.TextField(max_length=500, null=True)
    
    yard = models.ForeignKey(Person, related_name='i_as_y', on_delete=models.CASCADE)
    _class = models.ForeignKey(Person, related_name='i_as_c', on_delete=models.CASCADE)
    owner = models.ForeignKey(Person, related_name='i_as_o', on_delete=models.CASCADE)
    # property open:bool -> daca toate remarcile sunt inchise => opened = False
    