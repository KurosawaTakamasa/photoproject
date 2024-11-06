from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', include('photo.urls')),
    
    path('', include('accounts.urls')),
    
    path('password_reset/',
         auth_view.PasswordResetView.as_view(
             template_name = 'password_reset.html'),
         name='password_reset'),
    
    path('password_reset/done/',
         auth_view.PasswordResetDoneView.as_view(
             template_name = 'password_reset_sent.html'),
         name='password_reset_done'),
    
    path('sent/<uidb64>/<token>',
         auth_view.PasswordResetConfirmView.as_view(
             template_name = 'password_reset_form.html'),
         name='password_reset_confirm'),
    
    path('reset/done/',
         auth_view.PasswordResetCompleteView.as_view(
             template_name = 'password_reset_done.html'),
         name='password_reset_complete'),
]
