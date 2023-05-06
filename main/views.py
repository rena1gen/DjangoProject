from django.shortcuts import redirect
from django.shortcuts import render
from .forms import UserRegistrationForm
from .models import Person



# Create your views here.


def index(request):
    return render(request, "mainApp/html/data.html")


def about(request):
    return render(request, "mainApp/html/about.html")


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = Person.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
            )
            user.save()
            return redirect('registration_success')
    else:
        form = UserRegistrationForm()
    return render(request, 'mainApp/html/register.html', {'form': form})


def registration_success(request):
    return render(request, 'mainApp/html/registration_success.html')


