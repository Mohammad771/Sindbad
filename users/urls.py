from django.urls import path
from users import views

app_name = "users"

urlpatterns = [
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('admin/', views.admin, name='admin'),
    path('seller/', views.customer, name='seller'),
    path('customer/', views.employee, name='customer'),
]