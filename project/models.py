from django.db import models
from ccc.models import CCC, Person

class ProjectType(models.Model):
    class Meta:
        verbose_name = 'Type of Projects'
        verbose_name_plural = 'Types of Projects'
        
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
    gt = models.IntegerField(blank=True, null=True, verbose_name='Gross Tonage')
    dwt = models.IntegerField(blank=True, null=True, verbose_name='Deadweight')
    loa = models.IntegerField(blank=True, null=True, verbose_name='Length Overall')
    lpp = models.IntegerField(blank=True, null=True, verbose_name='Length between Perpendiculars')
    bb = models.IntegerField(blank=True, null=True, verbose_name='Breadth or Beam')
    draft = models.IntegerField(blank=True, null=True, )
    speed = models.IntegerField(blank=True, null=True, )
    capacity = models.IntegerField(blank=True, null=True, )
    crew = models.IntegerField(blank=True, null=True, )
    class_notation = models.CharField(blank=True, null=True, max_length=100)
    propulsion = models.CharField(blank=True, null=True, max_length=50)
    
    pm = models.ForeignKey(Person, related_name='pm_for', 
                           verbose_name='Project Manager', null=True, on_delete=models.SET_NULL)
    cm = models.ForeignKey(Person, related_name='cm_for', 
                           verbose_name='Construction Manager', blank=True, null=True, on_delete=models.SET_NULL)
    sm = models.ForeignKey(Person, related_name='sm_for', 
                           verbose_name='Site Manager', blank=True, null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return f'{self.id}: {self.name}'

class Discipline(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Element(models.Model):
    STATUS_CHOICES = [
        (0, 'Null'),
        (1, 'Mounted'), 
        (2, 'Fabricated')
    ]
    
    marking = models.CharField(max_length=50)
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE)
    mark = models.CharField(max_length=20)
    block = models.CharField(max_length=20, blank=True, null=True,)
    zone = models.CharField(max_length=20, blank=True, null=True,)
    deck = models.CharField(max_length=20, blank=True, null=True,)
    sys_desc = models.CharField(verbose_name='System Description', max_length=200, blank=True, null=True,)
    sys_nb = models.IntegerField(verbose_name='System Number SFI', blank=True, null=True,)
    alter = models.CharField(verbose_name='Alteration Sheet', max_length=20, blank=True, null=True,)
    status = models.IntegerField(choices=STATUS_CHOICES)
    inspection = models.ForeignKey('inspection.CCOS', blank=True, null=True, on_delete=models.SET_NULL)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    
    def get_status_display(self):
        return self.STATUS_CHOICES[self.status][1]
    
    def __str__(self):
        return self.marking