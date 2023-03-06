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

    def clean(self):
        link = self.link

        if not link.startswith("https://www."):
            raise ValidationError(
                {'link': "يجب ان يكون الرابط بهذه الصيغة: https://www.example.com"})


class category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=24)

    def __str__(self):
        return self.name


class allowed_seller_numbers(models.Model):
    id = models.AutoField(primary_key=True)
    phone_number = models.CharField(max_length=10, blank=True)
    is_available = models.BooleanField(default=True) # True if the number was already used to create a store
    user_id = models.ForeignKey("users.user", on_delete=models.CASCADE, related_name="+", null = True, default=None, blank=True) # which user has claimed this seller number

    def clean(self):
        phone_number = self.phone_number

        try:
            float(phone_number)
        except ValueError:
            raise ValidationError(
                {'phone_number': "يجب ان يحتوي رقم الجوال على أرقام فقط"})

        if (len(phone_number)<10):
            raise ValidationError(
                {'phone_number': "يجب ان يحتوي رقم الجوال على 10 خانات"})  
    
