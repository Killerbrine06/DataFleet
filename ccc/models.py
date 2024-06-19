from django.db import models
from django.contrib.auth.models import User

class Facility(models.Model):
    class Meta:
        verbose_name_plural = 'Facilities'
        
    yard = models.OneToOneField('CCC', on_delete=models.CASCADE)
    power = models.TextField(max_length=150)
    quay = models.TextField(max_length=150)
    outfit_hall = models.TextField(verbose_name='Outfitting Hall', max_length=150)
    workshop = models.TextField(max_length=300)
    bb = models.CharField(verbose_name='Building Berth', max_length=100)
    lifting = models.CharField(max_length=100)
    record = models.CharField(verbose_name='IACS UR Z23 Record', max_length=100)
    stategy = models.CharField(verbose_name='Construction Strategy', max_length=100)
    proc = models.CharField(verbose_name='Applicable Procedures', max_length=100)


class CCC(models.Model):
    class Meta:
        verbose_name = 'CCC'
        verbose_name_plural = 'CCCs'
        
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(null=True, max_length=500)
    year = models.IntegerField()
    director = models.ForeignKey('Person', null=True, on_delete=models.SET_NULL)
    phone = models.CharField(null=True, max_length=12)
    address = models.CharField(null=True, max_length=30)
    facilities = models.OneToOneField(Facility, null=True, on_delete=models.SET_NULL)
    subcontractor = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
class Person(models.Model):
    _user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(null=True, max_length=12)
    address = models.CharField(null=True, max_length=30)
    employer = models.ForeignKey(CCC, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self._user.first_name} {self._user.last_name}'
