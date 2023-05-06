from django.shortcuts import render
from .forms import UserRegistrationForm

# Create your views here.


def index(request):
    return render(request, "mainApp/html/data.html")


def about(request):
    return render(request, "mainApp/html/about.html")


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'mainApp/html/registration_success.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'mainApp/html/register.html', {'user_form': user_form})
