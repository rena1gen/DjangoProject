class MoneyForm(forms.ModelForm):
    class Meta:
        model = Money
        fields = ['FIO' , 'number' , 'email']

    def save(self, user, commit=True):
        message1 = super(MoneyForm, self).save(commit=False)
        message1.user = user
        if commit:
            message1.save()
        return message1
