from django.urls import path
from stores import views

app_name = "stores"
urlpatterns = [
    path('', views.home, name='home'),
    path('create_store/', views.create_store, name='create_store'),
    path('update_store/', views.update_store, name='update_store'),
    path('about_us/', views.about_us, name='about_us'),
    path('like/', views.like, name='like'),
    path('store/', views.store, name='store'),
]