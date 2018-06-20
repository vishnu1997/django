from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from myapp.forms import myprojectForm,CustomUserCreationForm
from myapp.models import myproject,groupreq
from myapp.forms import  LoginForm

# Create your views here.
def index(request):
    #myproject1 = myproject.objects.all()
    if request.user.is_superuser:
        return HttpResponseRedirect('/admin')
    elif request.user.is_authenticated:
        form = myprojectForm()
        return render(request, 'index.html', {'form':form})
    else:
        return HttpResponseRedirect('/login')

def post_resume(request):
    form = myprojectForm(request.POST)
    if form.is_valid():
        tr = myproject(
            name = form.cleaned_data['name'],
            regno = form.cleaned_data['regno'],
            cgpa = form.cleaned_data['cgpa'],
            email = form.cleaned_data['email'],
            location = form.cleaned_data['location'],
            img_url = form.cleaned_data['img_url']
        )
        tr.save()
    return HttpResponseRedirect('/show/')

def show(request):
    myproject1 = myproject.objects.all()
    return render(request , 'show.html',{'myprojecte':myproject1})

def newuser(request):
    if request.method == 'POST':
        f = CustomUserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            return HttpResponseRedirect('/superuser')

    else:
        f = CustomUserCreationForm()

    return render(request, 'newuser.html', {'form': f})
def superu(request):
    return render(request ,'superu.html',{})

def gandp(request):
    return render(request,'superu.html',{})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                # the password verified for the user
                if user.is_active:
                    print("User is valid, active and authenticated")
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    print("The password is valid, but the account has been disabled!")
            else:
                # the authentication system was unable to verify the username and password
                print("The username and password were incorrect.")

    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login')

 
def reqhr(request,usr):
    tr = groupreq(
        name = usr,
        groupReq = "HR"
    )
    tr.save()
    return render(request ,'requested.html',{})

def reqacc(request,usr):
    tr = groupreq(
        name = usr,
        groupReq = "accountant"
    )
    tr.save()
    return render(request ,'requested.html',{})