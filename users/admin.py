from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(region)
admin.site.register(city)
admin.site.register(seller)
admin.site.register(wholesaler)
admin.site.register(rep)
admin.site.register(allowed_seller_numbers)
