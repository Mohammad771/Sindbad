from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, wholesaler, rep

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
            # 'password_mismatch': ("يجب ان يتشابه حقل كلمة المرور مع تأكيد كلمة المرور"), doesn't work

            'email': {
                'required': ("الرجاء ادخال البريد الالكتروني بشكل صحيح"),
                'invalid': ("الرجاء ادخال البريد الالكتروني بشكل صحيح"),
                'unique': ("هذا البريد الالكتروني موجود مسبقاً"),
            },
            'username': {
                'unique': ("هذا البريد الالكتروني موجود مسبقاً"),
            },
            'first_name': {
                'required': ("الرجاء ادخال الاسم الأول بشكل صحيح"),
            },
            'last_name': {
                'required': ("الرجاء ادخال الأسم الأخير بشكل صحيح"),
            },
            'phone_number': {
                'required': ("الرجاء إدخال رقم الجوال بشكل صحيح، الصيغة الصحيحة: 0512345678"),
                'invalid': ("الرجاء إدخال رقم الجوال بشكل صحيح، الصيغة الصحيحة: 0512345678"),
                'max_length': ("يجب ان يحتوي رقم الجوال على 10 خانات فقط"),
            },

        }

class update_user_form(forms.ModelForm):

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone_number',)
        error_messages = {
            'email': {
                'required': ("الرجاء ادخال البريد الالكتروني بشكل صحيح"),
                'invalid': ("الرجاء ادخال البريد الالكتروني بشكل صحيح"),
            },
            'first_name': {
                'required': ("الرجاء ادخال الاسم الأول بشكل صحيح"),
            },
            'last_name': {
                'required': ("الرجاء ادخال الأسم الأخير بشكل صحيح"),
            },
            'phone_number': {
                'required': ("الرجاء إدخال رقم الجوال بشكل صحيح، الصيغة الصحيحة: 0512345678"),
                'invalid': ("الرجاء إدخال رقم الجوال بشكل صحيح، الصيغة الصحيحة: 0512345678"),
                'max_length': ("يجب ان يحتوي رقم الجوال على 10 خانات فقط"),
            },
        }
        
class create_wholesaler_form(forms.ModelForm):

    class Meta:
        model = wholesaler
        fields = ('business_name', 'products_types', 'description', 'city','store_photo',)
        error_messages = {
            'business_name': {
                'required': ("الرجاء إدخال اسم المؤسسة"),
            },
            'products_types': {
                'required': ("الرجاء إدخال انواع البضائع الخاصة بمؤسستك"),
            },
            'description': {
                'required': ("الرجاء إدخال وصف لمؤسستك ومنتجاتك"),
            },
        #    'store_photo': {
        #         'invalid_extension': ("يمكن رفع الصور فقط بالصيغات التالية: jpg, png"),
        #     },
        }

class create_rep_form(forms.ModelForm):

    class Meta:
        model = rep
        fields = ('city','photo',)
        error_messages = {
            'photo': {
                'invalid_extension': ("يمكن رفع الصور فقط بالصيغات التالية: jpg, png"),
            },
            # 'products_types': {
            #     'required': ("الرجاء ادخال انواع البضائع الخاصة بمؤسستك"),
            # },
            # 'descriptoin': {
            #     'required': ("الرجاء ادخال وصف لموسستك ومنتجاتك"),
            # },
            # 'phone_number': {
            #     'required': ("الرجاء إدخال رقم الهاتف بشكل صحيح، الصيغة الصحيحة: 0512345678"),
            #     'invalid': ("الرجاء إدخال رقم الهاتف بشكل صحيح، الصيغة الصحيحة: 0512345678"),
            # },
        }
