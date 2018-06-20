from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError

# Create your models here.
class myprojectForm(forms.Form):
    name = forms.CharField(label='name',max_length=100)
    regno = forms.DecimalField(label='regno',max_digits=13, decimal_places=0)
    cgpa = forms.DecimalField(label='cgpa',max_digits=13, decimal_places=4)
    email = forms.CharField(label='email',max_length=100)
    location = forms.CharField(label='location',max_length=100)
    img_url = forms.CharField(label='img_url',max_length=255)

class LoginForm(forms.Form):
    username = forms.CharField(label='User Name', max_length=64)
    password = forms.CharField(widget=forms.PasswordInput())

class cgroup(forms.Form):
    group = forms.CharField(label = 'groupname',max_length=40)
    permission = forms.CharField(label = 'permissionname',max_length=64)

class CustomUserCreationForm(forms.Form):
    username = forms.CharField(label='Enter Username', min_length=4, max_length=150)
    email = forms.EmailField(label='Enter email')
    password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise  ValidationError("Username already exists")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise  ValidationError("Email already exists")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")

        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user

