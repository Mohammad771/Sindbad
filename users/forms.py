from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

# class login_form(forms.Form):
#     email = forms.CharField(
#         widget = forms.TextInput(
#             attrs={
#                 "class":"form-control"
#             }
#         )
#     )

#     password = forms.CharField(
#         widget = forms.PasswordInput(
#             attrs={
#                 "class":"form-control"
#             }
#         )
#     )

class register_form(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2','first_name', 'last_name', 'phone_number',)
        error_messages = {
            'email': {
                'required': ("الرجاء ادخال البريد الالكتروني بشكل صحيح"),
            },
            'phone_number': {
                'required': ("الرجاء إدخال رقم الهاتف بشكل صحيح، الصيغة الصحيحة: 0512345678"),
                'invalid': ("الرجاء إدخال رقم الهاتف بشكل صحيح، الصيغة الصحيحة: 0512345678"),
            },
        }
