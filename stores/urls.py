from django.urls import path
from stores import views

app_name = "stores"
urlpatterns = [
    path('', views.home, name='home'),
    # path('store/', views.store, name='store'),
    # path('edit_store/', views.edit_store, name='edit_store'),
    path('about_us/', views.about_us, name='about_us'),
]