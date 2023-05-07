from django.shortcuts import redirect
from django.shortcuts import render

from .forms import RegistrationForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Redirect to success page or login page
            return redirect('mainApp/html/registration_success.html')
    else:
        form = RegistrationForm()
    return render(request, 'mainApp/html/register.html', {'form': form})

def index(request):
    return render(request, "mainApp/html/data.html")


def about(request):
    return render(request, "mainApp/html/about.html")


