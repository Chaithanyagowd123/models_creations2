from django.db import models

# Create your models here.
class Country(models.Model):
    cname=models.CharField(max_length=100,primary_key=True)


    def __str__(self):
        return self.cname

class Capital(models.Model):
    cname=models.ForeignKey(Country,on_delete=models.CASCADE)
    capitalName=models.CharField(max_length=100,unique=True)


    def __str__(self):
        return self.capitalName


