from django import forms

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
