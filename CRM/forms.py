from django import forms
from .models import Money
from django.forms import TextInput


class MoneyForm(forms.ModelForm):
    class Meta:
        model = Money
        fields = ['message', 'summa', 'date_of_add']
        widgets = {"message": TextInput(attrs={'class': 'task-input', 'placeholder': 'Введите название сделки'}),
                   "summa": TextInput(attrs={'class': 'task-input', 'placeholder': 'Введиту сумму'}),
                   "date_of_add": TextInput(attrs={'class': 'task-input', 'placeholder': 'Введите число'})
                   }

    def save(self, user, commit=True):
        message1 = super(MoneyForm, self).save(commit=False)
        message1.user = user
        if commit:
            message1.save()
        return message1
