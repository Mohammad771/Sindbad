from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from stores.models import Store
from django.core.validators import FileExtensionValidator





# Create your models here.


class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=24)
    last_name = models.CharField(max_length=24)
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    store_id = models.ForeignKey(Store, on_delete=models.CASCADE, related_name="+", null = True, default=None, blank=True)
    photo = models.FileField(null = True, default=None, blank=True, upload_to='static/upload/users_photos',
        validators=[FileExtensionValidator(allowed_extensions=['png','jpg',"jpeg"])])



    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(null = True, default=None, blank=True)
    deleted_at = models.DateTimeField(null = True, default=None, blank=True)

    is_admin = models.BooleanField("Admin", default=False)
    is_customer = models.BooleanField("Customer", default=False)
    is_seller = models.BooleanField("Seller", default=False)

    def __str__(self):
        return self.username 

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

