from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'Home.html')

def store_profile(request):
    return render(request,'stores/store_profile.html')
