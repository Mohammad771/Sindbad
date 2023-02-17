from django import forms
from .models import Store

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
