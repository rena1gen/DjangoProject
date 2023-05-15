from django import forms
from .models import Money

class MoneyForm(forms.ModelForm):
    class Meta:
        model = Money
        fields = ['message' , 'summa' , 'date_of_add']

    def save(self, user, commit=True):
        message1 = super(MoneyForm, self).save(commit=False)
        message1.user = user
        if commit:
            message1.save()
        return message1

