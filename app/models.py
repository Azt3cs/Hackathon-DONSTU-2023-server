
from django.db import models

class Pari(models.Model):
    predmet = models.CharField(max_length=35,blank=False)
    prepod = models.ForeignKey('Prepodi',on_delete=models.PROTECT)
    group = models.ForeignKey('Group',on_delete=models.PROTECT)
    date = models.DateTimeField()
    auditoria = models.ForeignKey('Aud', on_delete=models.PROTECT)
    def __str__(self):
        return f'{self.predmet}'

class Prepodi(models.Model):
    fio = models.CharField(max_length=50,blank=False,primary_key=True)

    def __str__(self):
        return f'{self.fio}'

class Group(models.Model):
    name = models.CharField(max_length=30,blank=False,primary_key=True,unique=True)

    def __str__(self):
        return f'{self.name}'

class Aud(models.Model):
    number = models.IntegerField(primary_key=True,unique=True)

    def __str__(self):
        return f'{self.number}'