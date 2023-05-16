from django.db.models import Sum
from django.shortcuts import render, redirect
from django.views import View
from .models import Money

from CRM.forms import MoneyForm


class MoneyView(View):
    template_name = 'mainApp/money.html'
    form_class = MoneyForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        if request.method == 'POST':
            form = MoneyForm(request.POST)
            task = Money.objects.filter(user=request.user)
            if form.is_valid():
                message = form.save(commit=False, user=request.user)
                message.user = request.user
                message.save()
                return render(request, self.template_name, {'form': MoneyForm(), 'task': task})
        return render(request, self.template_name, {'form': form})

    def calc(request):
        money = Money.objects.filter(user=request.user).aggregate(Sum('summa'))['summa__sum']
        task = Money.objects.filter(user=request.user)
        if request.method == 'POST':
            return render(request, 'mainApp/money.html', {'task': task, 'money':money})

    def delete(request):
        user = request.user
        data = Money.objects.filter(user=user)
        if request.method == 'POST':
            data.delete()
        for task in data:
            if task == task.delete():
                task.delete()
        return redirect('money')