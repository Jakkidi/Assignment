from django.db import models

# Create your models here.
class product(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    length=models.IntegerField()
    size=models.CharField(max_length=100)
    quality=models.CharField(max_length=100)

class cart(models.Model):
    added_at=models.DateField()
    producttitle=models.ForeignKey(product,on_delete=models.CASCADE)