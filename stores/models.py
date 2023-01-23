from django.db import models

# Create your models here.

class Store(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=24)
    descriptoin = models.TextField()
    link = models.CharField(max_length=300)
    city = models.ForeignKey('users.city', on_delete=models.CASCADE, related_name="+")
