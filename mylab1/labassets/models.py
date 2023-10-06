from django.db import models

# Create your models here.
class Asset(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    purchased_date = models.DateField()
    workflag = models.BooleanField(default=False)  

    def __str__(self):
        return self.name
