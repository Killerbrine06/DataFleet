from django.db import models
from ccc.models import CCC, Person

class ProjectType(models.Model):
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.type
    

class Docs(models.Model):
    pass

class Project(models.Model):
    name = models.CharField(max_length=30)
    yard = models.ForeignKey(CCC, related_name='yard_for', on_delete=models.CASCADE)
    owner = models.ForeignKey(CCC, related_name='owner_to', on_delete=models.CASCADE)
    _class = models.ForeignKey(CCC, related_name='class_to', verbose_name='Class', on_delete=models.CASCADE)
    # docs
    command_number = models.IntegerField()
    type = models.ForeignKey(ProjectType, on_delete=models.CASCADE)
    gt = models.IntegerField(verbose_name='Gross Tonage')
    dwt = models.IntegerField(verbose_name='Deadweight')
    loa = models.IntegerField(verbose_name='Length Overall')
    lpp = models.IntegerField(verbose_name='Length between Perpendiculars')
    bb = models.IntegerField(verbose_name='Breadth or Beam')
    draft = models.IntegerField()
    speed = models.IntegerField()
    capacity = models.IntegerField()
    crew = models.IntegerField()
    class_notation = models.CharField(max_length=100)
    propulsion = models.CharField(max_length=50)
    
    pm = models.ForeignKey(Person, related_name='pm_for', verbose_name='Project Manager', null=True, on_delete=models.SET_NULL)
    cm = models.ForeignKey(Person, related_name='cm_for', verbose_name='Construction Manager', null=True, on_delete=models.SET_NULL)
    sm = models.ForeignKey(Person, related_name='sm_for', verbose_name='Site Manager', null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return f'{self.id}: {self.name}'

class Discipline(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Element(models.Model):
    marking = models.CharField(primary_key=True, max_length=50)
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE)
    mark = models.CharField(max_length=20)
    block = models.CharField(max_length=20)
    zone = models.CharField(max_length=20)
    deck = models.CharField(max_length=20)
    sys_id = models.CharField(verbose_name='System Id', max_length=5)
    sys_nb = models.IntegerField(verbose_name='System Number SFI', )
    alter = models.CharField(verbose_name='Alteration Sheet', max_length=20)
    status = models.IntegerField(choices=[
            (0, 'Null'),
            (1, 'Inspected'),
            (2, 'Mounted'), 
            (3, 'Fabricated')
        ])
    project = models.ForeignKey(Project, on_delete=models.CASCADE)