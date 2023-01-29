from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import authenticate, login, logout as user_logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.core.mail import send_mail
from .models import allowed_seller_numbers, seller, city, wholesaler as wholesaler_model, rep as rep_model, User


# Create your views here.

def register(request):

    context = {}

    if request.method == "POST":
        request_post_copy = request.POST.copy()
        request_post_copy['username'] = request.POST['email']
        form = register_form(request_post_copy, request.FILES)

        if form.is_valid():
            form.save()
            email = request_post_copy['email']
            password = request_post_copy['password1']
            user = authenticate(request,username=email, password=password)

            if user is not None:
                # login(request, user)
                context["msg"] = "Login Successful"


                # ----------------- Checking if the registering user has a seller phone number-------------
                allowed_phone_numbers = allowed_seller_numbers.objects.filter(is_available=True) # fetching the allowed & unused phone numbers
                # print(allowed_phone_numbers)
                # print(user)
                for allowed_number in allowed_phone_numbers:
                    # print(allowed_number)
                    # print("from db: "+ allowed_number.phone_number)
                    # print("from request: "+request_post_copy['phone_number'])                    
                    if (allowed_number.phone_number == request_post_copy['phone_number']): # if the user's number was found in the allowed list
                        
                        try:
                            new_seller = seller() # create a new seller
                            new_seller.save() # save the change

                        except Exception as e:
                            print("There was an error while creating a new seller account, The error is:")
                            print(e)

                        try:
                            user.seller_id = new_seller # assign the new seller id to the new user account
                            user.save() # save the change

                        except Exception as e:
                            print("There was an error while assigning the new seller account to the user account, The error is:")
                            print(e)

                        try:
                            allowed_number.is_available = False # assign the number as taken
                            allowed_number.user_id = user
                            allowed_number.save() # save the change

                        except Exception as e:
                            print("There was an error while assigning the user to the seller number and making the seller number unavailable, The error is:")
                            print(e)

            return redirect('/')

        else:
            print(form.errors)
            context['errors'] =  form.errors
            context['form_errors'] = form
            # return redirect('/register')
            return render(request, 'users/register.html', context)


        

        
    return render(request, 'users/register.html', context)



def user_login(request):
    if request.user.is_authenticated:
        return redirect('/')

    if 'next' in request.GET:
        request.session['next'] = request.GET['next']

    context = {}

    if request.method == "POST":
        requried_page = request.GET.get('next', None)
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)
        if user:
            if user.is_active:
                login(request, user)
                if 'next' in request.session:
                    requested_url = request.session['next']
                    return redirect(requested_url)
                else:
                    return redirect('/')

            else:
                print("User is not yet activated")
                context['login_error'] = "User is not yet activated"
                return render(request, 'users/login.html', context)              
        
        else:
            print("incorrect credentials")
            context['msg'] = "البريد الالكتروني او كلمة المرور غير صحيحة"
            return render(request, 'users/login.html', context)
    
    else:
        return render(request, 'users/login.html')

@login_required
def logout(request):
    context = {}
    user_logout(request)
    context['msg'] = "Logout Successful"

    # send_mail(
    #     'Subject here',
    #     'Here is the message.',
    #     'from@example.com',
    #     ['mohmd.mohmds@gmail.com'],
    #     fail_silently=False,
    # )
    # print("email sent")
    # return HttpResponse("Success")
    # back_home(request,context)
    return redirect('/')
    # return HttpResponseRedirect('/logout')
    # return render(request, 'Home.html', context)


# def back_home(request, context=None):
#     return render(request,'Home.html', context)

# def forgot_password(request):

#     return render(request,'forgot_password.html')


def admin(request):
    return render(request,'admin.html')


def profile(request):
    return render(request,'users/profile.html')

def list_wholesalers(request):
    return render(request,'users/list_wholesalers.html')

def list_reps(request):
    context = {}

    context["rep_users"] = User.objects.filter(rep_id__isnull=False)
    return render(request,'users/list_reps.html', context)

def wholesaler(request):
    context = {} 

    if request.method == "POST": 
        form = create_wholesaler_form(request.POST, request.FILES)

        if form.is_valid():
            new_wholesaler = form.save()
            request.user.wholesaler_id = new_wholesaler
            request.user.save()
            context["msg"] = "تم انشاء حساب تاجر الجملة بنجاح"
        else:
            errors_array = []
            form_errors =  form.errors.get_json_data()
            # print(form_errors['business_name'][0]['message'])
            for key, errors in form_errors.items():
                for error in errors:
                    errors_array.append(error['message'])

            context['errors'] = errors_array

    context['cities'] = city.objects.all()
    return render(request,'users/wholesalers-form.html', context)
    

def rep(request):
    context = {} 

    if request.method == "POST": 
        print(request.POST)
        form = create_rep_form(request.POST, request.FILES)
        print(request.FILES)

        if form.is_valid():
            new_rep = form.save()
            request.user.rep_id = new_rep
            request.user.save()
            context["msg"] = "تم انشاء حساب المندوب بنجاح"
        else:
            errors_array = []
            form_errors =  form.errors.get_json_data()
            # print(form_errors['business_name'][0]['message'])
            for key, errors in form_errors.items():
                for error in errors:
                    errors_array.append(error['message'])

            context['errors'] = errors_array

    context['cities'] = city.objects.all()
    return render(request,'users/reps-form.html', context)

# def profile_edit(request):
#     return render(request,'edit_profile.html')


# def seller(request):
#     return render(request,'seller.html')


