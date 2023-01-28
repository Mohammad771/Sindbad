from django.urls import path
from users import views
from django.contrib.auth import views as auth_views 


app_name = "users"

urlpatterns = [
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),

    
    # __________________________________________________

    # Customer
    path('profile/', views.profile, name='profile'), # where all users can view and edit their data & see favorite stores
    # path('profile_edit/', views.profile_edit, name='profile_edit'), # where all users can edit their data
    # __________________________________________________

    # Seller
    # path('seller/', views.seller, name='seller'), # where he can edit his data
    path('wholesalers/', views.list_wholesalers, name='list_wholesalers'), # where seller can see all wholesalers
    path('reps/', views.list_reps, name='list_reps'), # where seller can see all reps


    # __________________________________________________

    # Wholesaler
    path('wholesaler-form/', views.wholesaler, name='wholesaler'), # where he can view his data

    # __________________________________________________
    
    # Representative
    path('rep-form/', views.rep, name='rep'), # where he can view his data & favorite stores

    # __________________________________________________

    # Admin
    # path('admin/', views.admin, name='admin'),

    # __________________________________________________

    path('password_reset/',auth_views.PasswordResetView.as_view(template_name =
    'users/password_reset_form.html') ,name='reset_password'),
    path('password_reset_done/',auth_views.PasswordResetDoneView.as_view(template_name =
    'users/password_reset_done.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name =
    'users/password_reset_confirm.html'),name='password_reset_confirm'),
    path('reset_done/',auth_views.PasswordResetCompleteView.as_view(template_name =
    'users/password_reset_complete.html'),name='password_reset_complete'),
]