from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from .forms import RegistrationForm
from .forms import MyLoginForm
from .models import MyTask
from .forms import MessageForm
from .models import MyUser


def login_view(request):
    if request.method == 'POST':
        form = MyLoginForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(request, email=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('taskmanager')
    else:
        form = MyLoginForm(request)
    return render(request, 'mainApp/html/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


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
            MyTask.objects.filter(id__in=request.POST.getlist('selected_items')).delete()
            return redirect('taskmanager')
        else:
            items = MyTask.objects.all()
            return render(request, 'mainApp/html/delete_selected.html', {'items': items})



def index(request):
    return render(request, "mainApp/html/data.html")


def about(request):
    return render(request, "mainApp/html/about.html")
