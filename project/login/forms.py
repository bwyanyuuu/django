from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm, PasswordChangeForm
from django.contrib.auth.models import User
from main.models import MyUser

class RegisterForm(UserCreationForm):
    class Meta:
        model = MyUser
    username = forms.CharField(
        required=True,
        label="Username",
        widget=forms.TextInput({'placeholder':'Username'})
    )
    email = forms.EmailField(
        required=True,
        label="Email",
        widget=forms.EmailInput({'placeholder':'Email'})
    )
    password1 = forms.CharField(
        required=True,
        label="Password",
        widget=forms.PasswordInput({'placeholder':'Password'})
    )
    password2 = forms.CharField(
        required=True,
        label="Comfirm Password",
        widget=forms.PasswordInput({'placeholder':'Comfirm Password'})
    )
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class LoginForm(forms.Form):
    class Meta:
        model = MyUser
    username = forms.CharField(
        required=True,
        label="Email",
        widget=forms.TextInput({'placeholder':'Email'})
    )
    password = forms.CharField(
        required=True,
        label="Password",
        widget=forms.PasswordInput({'placeholder':'Password'})
    )

class PasswdResetForm(PasswordResetForm):
    class Meta:
        model = MyUser
        fields = ('email')
    email = forms.EmailField(
        required=True,
        label='Email', 
        widget=forms.EmailInput({'placeholder': 'Email'})
    )

class PasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = MyUser
    old_password = forms.CharField(
        required=True,
        label="Old Password",
        widget=forms.PasswordInput({'placeholder':'Old Password'})
    )
    new_password1 = forms.CharField(
        required=True,
        label="New Password",
        widget=forms.PasswordInput({'placeholder':'New Password'})
    )
    new_password2 = forms.CharField(
        required=True,
        label="Confirm",
        widget=forms.PasswordInput({'placeholder':'Confirm New Password'})
    )

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ['first_name', 'middle_name', 'last_name', 'affiliation']
    first_name = forms.CharField(
        required=False,
        label="First Name"
    )
    middle_name = forms.CharField(
        required=False,
        label="Middle Name"
    )
    last_name = forms.CharField(
        required=False,
        label="Last Name"
    )
    affiliation = forms.CharField(
        required=False,
        label="Affiliation"
    )