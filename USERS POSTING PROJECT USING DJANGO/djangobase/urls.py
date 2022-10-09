"""djangobase URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path,include
from users import views as users_view
from django.contrib.auth import views as auth_view # login  

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls, name='login'),
    path('', include('playground.urls')),    
    path('register/', users_view.register, name='register'),
    path('login/', auth_view.LoginView.as_view(template_name='training/login.html' ) , name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='training/logout.html') , name='logout'),
    path('profile/', users_view.profile, name='profile'),
#--------------------------password reset paths-----------------------------------------------------------   

#template path = password_reset--> password_reset_done--> password_reset_confirm--> password_reset_complete

    path('password-reset/', 
         auth_view.PasswordResetView.as_view(template_name='training/password_reset.html'),
         name='password_reset'),
    
    path('password-reset/done/', 
         auth_view.PasswordResetDoneView.as_view(template_name='training/password_reset_done.html'),
         name='password_reset_done'),
    
    path('password-reset-confirm/<uidb64>/<token>/', 
         auth_view.PasswordResetConfirmView.as_view(template_name='training/password_reset_confirm.html'),
         name='password_reset_confirm'),

    path('password-reset-complete/', 
         auth_view.PasswordResetCompleteView.as_view(template_name='training/password_reset_complete.html'),
         name='password_reset_complete'),

#--------------------------password reset paths-----------------------------------------------------------    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# THIS IS FOR PROFILE TO SUPPORT ANY FORMAT AND PUT ALL PHOTO IN media[folder] WHICH IS CREATED BY VS CODE AND SHOULD PUT AN DEFAULT IMAGE 

