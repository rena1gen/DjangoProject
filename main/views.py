from django.contrib.auth import authenticate
from django.shortcuts import redirect
from django.shortcuts import render
from .models import Person
from .forms import RegistrationForm
from .forms import MyLoginForm
from django.contrib.auth import authenticate, login,logout


def login_view(request):
    if request.method == 'POST':
        form = MyLoginForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(request, email=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('about')
    else:
        form = MyLoginForm(request)
    return render(request, 'mainApp/html/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')




# Create your views here.


def index(request):
    return render(request, "mainApp/html/data.html")


def about(request):
    return render(request, "mainApp/html/about.html")


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # user = Person.objects.create_user(
            #     username=form.cleaned_data['username'],
            #     email=form.cleaned_data['email'],
            #     password=form.cleaned_data['password'],
            # )
            form.save()
            return render(request, 'mainApp/html/data.html')
    else:
        form = RegistrationForm()
    return render(request, 'mainApp/html/register.html', {'form': form})




