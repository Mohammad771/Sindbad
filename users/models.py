from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from stores.models import Store
from django.core.validators import FileExtensionValidator, ValidationError


# Create your models here.


class region(models.Model):
    name_ar = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100)
    id = models.IntegerField(primary_key=True)

    def __str__(self):
        return self.name_ar 

class city(models.Model):
    id = models.IntegerField(primary_key=True)
    name_ar = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100)
    region_id = models.IntegerField()

    def __str__(self):
        return self.name_ar 
    

class seller(models.Model):
    id = models.AutoField(primary_key=True)
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+")
    store_id = models.ForeignKey(Store, on_delete=models.CASCADE, related_name="+", null = True, default=None, blank=True)
    

class wholesaler(models.Model):
    id = models.AutoField(primary_key=True)
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+")
    products_types = models.CharField(max_length=500)
    products_descriptoin = models.TextField()
    city = models.ForeignKey(city, on_delete=models.CASCADE, related_name="+")


class rep(models.Model):
    id = models.AutoField(primary_key=True)
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+")
    city = models.ForeignKey(city, on_delete=models.CASCADE, related_name="+")

class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=24)
    last_name = models.CharField(max_length=24)
    username = models.CharField(max_length=30, unique=True)
    phone_number = models.CharField(max_length=10, blank=True)
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    photo = models.FileField(null = True, default=None, blank=True, upload_to='static/upload/users_photos',
        validators=[FileExtensionValidator(allowed_extensions=['png','jpg',"jpeg"])])

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(null = True, default=None, blank=True)
    deleted_at = models.DateTimeField(null = True, default=None, blank=True)

    is_admin = models.BooleanField("Admin", default=False)
    seller_id = models.ForeignKey(seller, on_delete=models.CASCADE, related_name="+", null = True, default=None, blank=True)
    wholesaler_id = models.ForeignKey(wholesaler, on_delete=models.CASCADE, related_name="+", null = True, default=None, blank=True)
    rep_id = models.ForeignKey(rep, on_delete=models.CASCADE, related_name="+", null = True, default=None, blank=True)
    # is_customer = models.BooleanField("Customer", default=False) (All users are customers)


    def __str__(self):
        return self.username 

    def clean(self):
        phone_number = self.phone_number

        try:
            float(phone_number)
        except ValueError:
            raise ValidationError(
                {'phone_number': "يجب ان يحتوي رقم الجوال على أرقام فقط"})

    # def save(self, *args, **kwargs):
    #     self.username = self.email
    #     super(Parcel, self).save(*args, **kwargs)


















# class User(AbstractUser):
#     class Role(models.TextChoices):
#         CUSTOMER = "CUSTOMER", 'Customer'
#         SELLER = "SELLER", 'Seller'
#         REP = "REP", 'Rep'
#         WHOLESALER = "WHOLESALER", 'Wholesaler'
#         ADMIN = "ADMIN", 'Admin'

#     base_role = Role.CUSTOMER
#     role = models.CharField(max_length=50, choices = Role.choices)
