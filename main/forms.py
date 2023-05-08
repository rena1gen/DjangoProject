from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


class MyLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus': True}))
    password = forms.CharField(widget=forms.PasswordInput)


class RegistrationForm(forms.ModelForm):
    email = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'popup-text'}), label='Введите пароль')
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'popup-text'}),required=False, label='Имя пользователя')

    class Meta:
        model = User
        fields = ('email', 'password', 'username')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
