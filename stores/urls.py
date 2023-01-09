from django.urls import path
from stores import views

app_name = "stores"
urlpatterns = [
    path('', views.home, name='home'),
    path('store_profile/', views.store_profile, name='store_profile'),

]