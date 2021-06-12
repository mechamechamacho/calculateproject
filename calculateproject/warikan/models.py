from django.db import models

# Create your models here.

class WarikanModel(models.Model):
    sum = models.IntegerField()
    anum = models.IntegerField()
    bnum = models.IntegerField()
    cnum = models.IntegerField()
    diffab = models.IntegerField()
    diffac = models.IntegerField()
    postdate = models.DateField(auto_now_add=True)
