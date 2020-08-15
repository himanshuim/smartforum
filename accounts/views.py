from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect
from .forms import LoginForm,RegisterForm
from django.contrib import messages

# Create your views here.


def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        'form': form
    }
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            print('Error')
    return render(request, 'login.html', context)
def register_page(request):
    print("@@@@@@@@@@@@@")
    form=RegisterForm()
    context = {
            'form': form
        }
    if request.method == 'POST':
        form=RegisterForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            if password1 != password2:
            print('###########')
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username already Taken')
                return redirect('accounts/register.html')
                #print('username taken')
            elif User.objects.filter(email=email).exists():
                #print('email exists')  
                messages.info(request,'E-mail already Taken')  
                return redirect('accounts/register.html')    
            else:
                user = User.objects.create_user(username=username,email=email,password1=password1,password2=password2)
                user.save()
                return redirect('/')
    return render(request, 'register.html', context)

