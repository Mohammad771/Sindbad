from django.shortcuts import render, redirect
from django.db import connection
from users.models import city, region
from .forms import *
# Create your views here.

def home(request):
    # cursor = connection.cursor()
    # cursor.execute("")
    return render(request,'Home.html')

def store(request):
    return render(request,'stores/store.html')

def create_store(incoming_reqest):
    context = {} 

    form = store_creation_form(incoming_reqest.POST, incoming_reqest.FILES)

    if form.is_valid():
        new_store = form.save()

        try:
            seller_account = incoming_reqest.user.seller_id
            seller_account.store_id = new_store
            seller_account.save()

            context["msg"] = "تم انشاء المتجر بنجاح"
            context["status"] = True
        except Exception as e:
            print("There was an error while assigning the new store to the seller, The error is:")
            print(e)

            new_store.delete()

            context["status"] = False
            context['errors'] = ['حدث خطأ اثناء إنشاء المتجر، رمز الخطأ: stores_profile_37']

    else:
        context["status"] = False
        errors_array = []
        form_errors =  form.errors.get_json_data()
        # print(form_errors['business_name'][0]['message'])
        for key, errors in form_errors.items():
            for error in errors:
                errors_array.append(error['message'])

        context['errors'] = errors_array

    return context

def update_store(incoming_reqest):
    context = {}

    form = store_creation_form(incoming_reqest.POST, incoming_reqest.FILES, instance=incoming_reqest.user.seller_id.store_id)

    if form.is_valid():
        form.save()
        context["msg"] = "تم تعديل المتجر بنجاح"
        context["status"] = True
    else:
        context["status"] = False
        errors_array = []
        form_errors =  form.errors.get_json_data()
        print(form_errors)
        # print(form_errors['business_name'][0]['message'])
        for key, errors in form_errors.items():
            for error in errors:
                errors_array.append(error['message'])

        context['errors'] = errors_array

    return context


    return render(request,'users/profile.html')

# def edit_store(request):
#     return render(request,'main/about_us.html')

def about_us(request):
    return render(request,'main/about_us.html')


