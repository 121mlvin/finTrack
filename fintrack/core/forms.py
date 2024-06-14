from allauth.account.forms import SignupForm
from django import forms
from .models import Account, Expense


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['balance', 'profile_picture']
        widgets = {
            'balance': forms.NumberInput(attrs={'class': 'form-control'}),
            'profile_picture': forms.FileInput(attrs={'class': 'form-control'}),
        }


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['price', 'description', 'expense_type']


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['profile_picture', 'balance']


class CustomSignupForm(SignupForm):
    balance = forms.DecimalField(max_digits=10, decimal_places=2)
    profile_picture = forms.ImageField(required=False)

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        balance = self.cleaned_data['balance']
        profile_picture = self.cleaned_data.get('profile_picture')
        account = Account.objects.create(user=user, balance=balance)

        if profile_picture:
            account.profile_picture = profile_picture
            account.save()

        return user
