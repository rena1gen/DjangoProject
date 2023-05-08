from django.shortcuts import redirect
from django.shortcuts import render
from .models import Person
from .forms import RegistrationForm




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
            return redirect('registration_success')
    else:
        form = RegistrationForm()
    return render(request, 'mainApp/html/register.html', {'form': form})


def registration_success(request):
    return render(request, 'mainApp/html/registration_success.html')



