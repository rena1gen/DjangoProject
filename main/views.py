
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.views.decorators.http import require_POST
from django.views.generic import View
from .forms import RegistrationForm
from .forms import MyLoginForm
from .models import MyTask, Order
from .forms import MessageForm
from datetime import date


def login_view(request):
    if request.method == 'POST':
        form = MyLoginForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(request, email=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return render(request, 'mainApp/html/Account.html')
    else:
        form = MyLoginForm(request)
    return render(request, 'mainApp/html/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('index')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Redirect to success page or login page
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'mainApp/html/register.html', {'form': form})


class MyTasks(View):
    form_class = MessageForm
    template_name = 'mainApp/html/message.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        if request.method == 'POST':
            form = MessageForm(request.POST)
            task = MyTask.objects.filter(user=request.user)
            if form.is_valid():
                message = form.save(commit=False, user=request.user)
                message.user = request.user
                if message.due_date < date.today():
                    message.is_overdue = True
                else:
                    message.is_overdue = False
                # привязываем сообщение к текущему пользователю
                message.save()
                return render(request, self.template_name, {'form': MessageForm(), 'task': task})
        return render(request, self.template_name, {'form': form})

    def delete_data(request):
        user = request.user
        data = MyTask.objects.filter(user=user)
        i = 0
        if request.method == 'POST':
            for task in data:
                i += 1
                if i == id:
                    task.delete()
        return redirect('taskmanager')

    def delete_selected(request):
        if request.method == 'POST':
            MyTask.objects.filter(user=request.user)
            MyTask.objects.filter(id__in=request.POST.getlist('selected_items')).delete()
            return redirect('taskmanager')
        else:
            items = MyTask.objects.all()
            return render(request, 'mainApp/html/delete_selected.html', {'items': items})


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Важно обновить пароль в сессии
            return redirect('login')
        else:
            messages.error(request, 'Попробуйте снова.', extra_tags='alert alert-danger')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'mainApp/html/change_passwort.html', {'form': form})


def index(request):
    return render(request, "mainApp/html/data.html")


def about(request):
    return render(request, "mainApp/html/features.html")

def price(request):
    return render(request, "mainApp/html/pricing.html")



def purchase(request):
    email = request.POST.get('email_id')
    if Order.objects.get(email=email):
        purchase = Order.objects.get(email=email)
        purchase.paid = True
        purchase.save()
        return render(request, 'mainApp/html/Account.html')
    else:
        return render(request , 'mainApp/html/login.html')


