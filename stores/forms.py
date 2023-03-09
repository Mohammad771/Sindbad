from django import forms
from .models import Store, allowed_seller_numbers

class store_creation_form(forms.ModelForm):

    class Meta:
        model = Store
        fields = ('name','description', 'link', 'store_photo', 'city', 'categories')
        error_messages = {
            'name': {
                'required': ("الرجاء إدخال اسم المتجر"),
            },
            'description': {
                'required': ("الرجاء إدخال وصف المتجر"),
            },
            'link': {
                'required': ("الرجاء إدخال رابط المتجر"),
            },
        }

class allowed_number_form(forms.ModelForm):

    class Meta:
        model = allowed_seller_numbers
        fields = ('phone_number',)
        error_messages = {
            'phone_number': {
                'required': ("الرجاء إدخال رقم الجوال بشكل صحيح، الصيغة الصحيحة: 0512345678"),
                'invalid': ("الرجاء إدخال رقم الجوال بشكل صحيح، الصيغة الصحيحة: 0512345678"),
                'max_length': ("يجب ان يحتوي رقم الجوال على 10 خانات فقط"),
                'unique': ("تمت إضافة هذا الرقم من قبل، الرجاء إدخال رقم آخر"),
            },
        }