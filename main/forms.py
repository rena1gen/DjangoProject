from django import forms
from django.forms import TextInput
from .models import MyTask

from .models import MyUser
from django.contrib.auth.forms import AuthenticationForm


class MyLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus': True}))
    password = forms.CharField(widget=forms.PasswordInput)
class RegistrationForm(forms.ModelForm):
    email = forms.EmailField(required=True, label='Email')
    password = forms.CharField(widget=forms.PasswordInput(), label='Пароль')
    username = forms.CharField(required=False, label='Имя пользователя')

    class Meta:
        model = MyUser
        fields = ('email', 'password', 'username')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


from .models import MyTask


class MessageForm(forms.ModelForm):
    due_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = MyTask
        fields = ['message', 'due_date']
        widgets = {"message": TextInput(attrs={'class': 'task-input', 'placeholder': 'Введите напоминание'}),

                   }

    def save(self, user, commit=True):
        message1 = super(MessageForm, self).save(commit=False)
        message1.user = user
        if commit:
            message1.save()
        return message1

