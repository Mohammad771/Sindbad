from django.shortcuts import render, redirect
from .forms import register_form
from django.contrib.auth import authenticate, login, logout as user_logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.core.mail import send_mail


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
            print(email)
            print(password)
            user = authenticate(request,username=email, password=password)
            if user is not None:
                login(request, user)
                context["msg"] = "Login Successful"
            else:
                print("user not found")
                context["msg"] = "user not found"

            return redirect('/')

        else:
            print(form.errors)
            context['errors'] =  form.errors
            context['form_errors'] = form
            # return redirect('/register')
            return render(request, 'users/register.html', context)

            
    else: #GET request
        
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
        password = request.POST.get('password1')

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
            context['msg'] = "incorrect credentials"
            return render(request, 'users/login.html', context)
    
    else:
        return render(request, 'users/login.html')

@login_required
def logout(request):
    context = {}
    user_logout(request)
    context['msg'] = "Logout Successful"

    send_mail(
        'Subject here',
        'Here is the message.',
        'from@example.com',
        ['mohmd.mohmds@gmail.com'],
        fail_silently=False,
    )
    print("email sent")
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
    return render(request,'profile.html')

def list_wholesalers(request):
    return render(request,'users/list_wholesalers.html')

def list_reps(request):
    return render(request,'users/list_reps.html')


# def profile_edit(request):
#     return render(request,'edit_profile.html')


# def seller(request):
#     return render(request,'seller.html')


# def wholesaler(request):
#     return render(request,'wholesaler.html')
    

# def rep(request):
#     return render(request,'rep.html')