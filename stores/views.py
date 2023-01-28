from django.shortcuts import render
from django.db import connection
from users.models import city, region
# Create your views here.

def home(request):
    # cursor = connection.cursor()
    # cursor.execute("")
    return render(request,'Home.html')

def store(request):
    return render(request,'stores/store.html')

# def edit_store(request):
#     return render(request,'main/about_us.html')

def about_us(request):
    return render(request,'main/about_us.html')


