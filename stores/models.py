from django.db import models
from django.core.validators import FileExtensionValidator, ValidationError


# Create your models here.

class Store(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=24)
    description = models.TextField()
    link = models.CharField(max_length=300)
    store_photo = models.FileField(null = True, default=None, blank=True, upload_to='static/upload/sellers_stores_photos',
        validators=[FileExtensionValidator(allowed_extensions=['png','jpg',"jpeg"],message="يمكن رفع الصور فقط بالصيغات التالية: (jpg, png, jpeg)")])
    city = models.ForeignKey('users.city', on_delete=models.CASCADE, related_name="+")
    categories = models.ManyToManyField('category', blank=True, related_name="+")
    likes = models.IntegerField(default=0)


class category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=24)

    def __str__(self):
        return self.name
    
