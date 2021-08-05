from django.db import models

class logTres(models.Model):
    id = models.AutoField(primary_key=True)
    date_created = models.DateField()
    key= models.CharField(max_length=40)
    value = models.FloatField()
