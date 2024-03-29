from django.shortcuts import render, redirect, HttpResponse
from django.db import connection
from users.models import city, region
from .forms import *
from .models import Store, category as categories_model, allowed_seller_numbers
from django.contrib.auth.decorators import login_required

# Db query execute:
# cursor = connection.cursor()
# cursor.execute('''''')

# How to develop ads

def home(request):

    context = {}
    context['home'] = True
    top_stores = Store.objects.order_by('-likes')[:6]
    all_stores = Store.objects.all()

    categories = categories_model.objects.all()
    top_3_categories = []
    try:
        top_3_categories.append(categories_model.objects.get(pk=1)) #الكترونيات
        top_3_categories.append(categories_model.objects.get(pk=4)) #حلويات
        top_3_categories.append(categories_model.objects.get(pk=6)) #ألبسة
    except:
        print('There are no categories in the database!')


    context['top_stores'] = top_stores
    context['all_stores'] = all_stores
    context['top_3_categories'] = top_3_categories
    context['categories'] = categories
    return render(request,'Home.html', context)

def allowed_numbers(request):
    context = {}
    msg = {}
    context['msg'] = msg

    if request.method == 'POST':

        form = allowed_number_form(request.POST)

        if form.is_valid():
            form.save()
            msg['type'] = 'success'
            msg['content'] = 'تمت إضافة الرقم بنجاح'
        else:
            errors_array = []
            form_errors =  form.errors.get_json_data()
            print(form_errors)
            first_error_key = list(form_errors.keys())[0]
            # print(form_errors['business_name'][0]['message'])
            for key, errors in form_errors.items():
                for error in errors:
                    errors_array.append(error['message'])

            context['errors'] = errors_array
            msg['type'] = 'error'
            msg['content'] = form_errors[first_error_key][0]['message']



    context['numbers'] = allowed_seller_numbers.objects.all()
    return render(request,'stores/store-management.html', context)


@login_required
def create_store(incoming_reqest):
    context = {}

    categories = incoming_reqest.POST.getlist('categories[]')
    form = store_creation_form(incoming_reqest.POST, incoming_reqest.FILES)

    if form.is_valid():
        new_store = form.save()

        for category in categories:
            new_store.categories.add(categories_model.objects.get(pk=category))
        new_store.save()
        

        try:
            seller_account = incoming_reqest.user.seller_id
            seller_account.store_id = new_store
            seller_account.save()

            context['msg'] = 'تم انشاء المتجر بنجاح'
            context['status'] = True
        except Exception as e:
            print('There was an error while assigning the new store to the seller, The error is:')
            print(e)

            new_store.delete()

            context['status'] = False
            context['errors'] = ['حدث خطأ اثناء إنشاء المتجر، رمز الخطأ: stores_profile_37']

    else:
        context['status'] = False
        errors_array = []
        form_errors =  form.errors.get_json_data()
        # print(form_errors['business_name'][0]['message'])
        for key, errors in form_errors.items():
            for error in errors:
                errors_array.append(error['message'])

        context['errors'] = errors_array
        context['returned_data'] = form.cleaned_data
    return context

@login_required
def update_store(incoming_reqest):
    context = {}

    categories = incoming_reqest.POST.getlist('categories[]')
    form = store_creation_form(incoming_reqest.POST, incoming_reqest.FILES, instance=incoming_reqest.user.seller_id.store_id)

    if form.is_valid():
        updated_store = form.save()

        for category in categories_model.objects.all():
            if str(category.id) in categories:
                updated_store.categories.add(category)
            else:
                updated_store.categories.remove(category)
        updated_store.save()


        context['msg'] = 'تم تعديل المتجر بنجاح'
        context['status'] = True
    else:
        context['status'] = False
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


def about_us(request):
    return render(request,'main/about_us.html')


def like(request):

    if request.user.is_authenticated:
        store_id = request.POST['store_id'] # get the id of the job title to be changed
        selected_store = Store.objects.get(pk=store_id) # fetch the job title row that the user wants to change

        if selected_store in request.user.liked_stores.all():
            request.user.liked_stores.remove(selected_store)
            request.user.save()

            selected_store.likes = selected_store.likes - 1
            selected_store.save() # saving the changes
            html = 'disliked'

        else:
            selected_store.likes = selected_store.likes + 1
            selected_store.save() # saving the changes

            request.user.liked_stores.add(selected_store)
            request.user.save()
            html = 'liked' # a variable that contains a success message to be sent as an http respone back to ajax function
            
        return HttpResponse(html) # returning 'success' as an http response because an error is produced when noting is returned.

    else:
        html = 'not signed in' # a variable that contains a success message to be sent as an http respone back to ajax function
        return HttpResponse(html) # returning 'success' as an http response because an error is produced when noting is returned.


