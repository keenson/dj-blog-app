from django.urls import path
from .views import UserRegisterView, PasswordsChangeView, UserEditView
from django.contrib.auth import views as auth_views
from . import views



urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    # path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html')),
    path('password/', PasswordsChangeView.as_view(template_name='registration/change-password.html')),
    path('password_success/', views.password_success, name='password_success'),
    
    
    path('reset_password/',  auth_views.PasswordResetView.as_view(), name='reset_password'),
    
    path('reset_password/',  auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    
    path('reset/<uidb64>/<token>',  auth_views.PasswordResetConfirmView.as_view(), name='password_reset_comfirm'),
    
    path('reset_password_complete/',  auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]
