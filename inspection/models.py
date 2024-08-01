import datetime
from django.db import models
from ccc.models import Person
from project.models import Project, Element, Discipline
from django.core.exceptions import ValidationError

# Yard - 0
# Class - 1
# Owner - 2

def check_type_yard(value:int):
    value = Person.objects.get(id=value)
    if value.employer.type != 0:
        raise ValidationError(f'The selected user is not part of a YARD type CCC')
   
def check_type_class(value:int):
    value = Person.objects.get(id=value)
    if value.employer.type != 1:
        raise ValidationError(f'The selected user is not part of a CLASS type CCC')

def check_type_owner(value:int):
    value = Person.objects.get(id=value)
    if value.employer.type != 2:
        raise ValidationError(f'The selected user is not part of a OWNER type CCC')
    

class Remark(models.Model):
    element = models.ForeignKey(Element, on_delete=models.CASCADE)
    inspection = models.ForeignKey('CCOS', on_delete=models.CASCADE)
    body = models.TextField(max_length=400)
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
    # class_inspection_date_closed = models.DateField(null=True) TODO property
    owner_inspection_date = models.DateField(null=True)
    # owner_inspection_date_closed = models.DateField(null=True) TODO property
    
    discipline = models.ForeignKey(Discipline, null=True, on_delete=models.SET_NULL)
    description = models.TextField(max_length=500, null=True)
    
    yard = models.ForeignKey(Person, validators=[check_type_yard], related_name='i_as_y', on_delete=models.CASCADE)
    u_class = models.ForeignKey(Person, validators=[check_type_class], verbose_name='Class', related_name='i_as_c', on_delete=models.CASCADE)
    owner = models.ForeignKey(Person, validators=[check_type_owner], related_name='i_as_o', on_delete=models.CASCADE)
    # property open:bool -> daca toate remarcile sunt inchise => opened = False
    