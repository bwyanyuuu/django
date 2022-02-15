from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import *
from django.core.mail import send_mail, BadHeaderError
from django.core.mail import EmailMessage
from django.conf import settings
from main.models import MyUser
from django.contrib.auth import get_user_model
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes

UserModel = get_user_model()

def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/virtual/accounts/login')
    context = {
        'form': form
    }
    return render(request, 'register.html', context)

def log_in(request):
    form = LoginForm()
    error = ''
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        if UserModel.objects.filter(Q(username=username)).exists():
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/virtual')
            else:
                error = 'Sorry, your password is incorrect. Please try again.'
        else:
            error = 'Sorry, that email is not registered. Please try again.'
        
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'login.html', context)

def log_out(request):
    logout(request)
    return redirect('/virtual/accounts/login')

def passwdReset(request):
    form = PasswdResetForm()
    if request.method == "POST":
        form = PasswdResetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data['email']
            associated_users = MyUser.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    c = {
                        "email":user.email,
                        'domain':'icmr2021.org',
                        'site_name': 'ACM ICMR 2021 Virtual',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'https',
                    }
                    email_template = render_to_string("password_reset_email.txt", c)
                    email = EmailMessage(
                        "Password Reset Requested From ICMR 2021 Virtual",  # 電子郵件標題
                        email_template,  # 電子郵件內容
                        settings.EMAIL_HOST_USER,  # 寄件者
                        [user.email]  # 收件者
                    )
                    # send_mail(
                    #     "Password Reset Requested From ICMR 2021 Virtual",
                    #     email_template,
                    #     settings.EMAIL_HOST_USER,
                    #     [user.email],
                    #     fail_silently=False,
                    # )
                    email.fail_silently = False
                    try:
                        email.send()
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect ("/virtual/password_reset/done/")
    context = {
        'form': form
    }
    return render(request, 'password_reset.html', context)

def passwdResetDone(request):
    return render(request, 'password_reset_done.html')
