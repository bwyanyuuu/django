"""project URL Configuration

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
from django.urls import path
from django.conf.urls.static import static

from django.conf.urls import include
from django.contrib.auth import views as auth_views
from login.views import *
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', log_in),
    path('accounts/logout/', log_out),
    path('accounts/password_reset/', passwdReset),
    path('password_reset/done/', passwdResetDone),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),  
    path('accounts/register/', register),
    path('', index),
    path('schedule/', schedule),
    path('session/', session),
    path('profile/', profile),
    path('edit_profile/', editProfile),
    path('change_password/', changePasswd)
]
urlpatterns  +=  static('/static/', document_root=settings.STATICFILES_DIRS[0]) 
# urlpatterns  +=  static('/static/admin/', document_root=settings.STATICFILES_DIRS[0]) 
# urlpatterns  +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
