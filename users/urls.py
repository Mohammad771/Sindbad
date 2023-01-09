from django.urls import path
from users import views
from django.contrib.auth import views as auth_views 


app_name = "users"

urlpatterns = [
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    # path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('admin/', views.admin, name='admin'),
    path('seller/', views.customer, name='seller'),
    path('customer/', views.employee, name='customer'),

    path('password_reset/',auth_views.PasswordResetView.as_view(template_name =
    'users/password_reset_form.html') ,name='reset_password'),

    path('password_reset_done/',auth_views.PasswordResetDoneView.as_view(template_name =
    'users/password_reset_done.html'),name='password_reset_done'),

    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name =
    'users/password_reset_confirm.html'),name='password_reset_confirm'),

    path('reset_done/',auth_views.PasswordResetCompleteView.as_view(template_name =
    'users/password_reset_complete.html'),name='password_reset_complete'),
]