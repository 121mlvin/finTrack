from django.contrib.auth.models import User
from django.db import models


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    profile_picture = models.ImageField(upload_to='pfps/', null=True, blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "Account"
        verbose_name_plural = "Accounts"


class Expense(models.Model):
    EXPENSE_TYPES = [
        ('Clothes', 'Clothes'),
        ('Food', 'Food'),
        ('Transport', 'Transport'),
        ('Entertainment', 'Entertainment'),
        ('Other', 'Other'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='expenses')
    date_of_spending = models.DateField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255, null=True, blank=True)
    expense_type = models.CharField(max_length=50, choices=EXPENSE_TYPES)

    def __str__(self):
        return f'{self.user.username} - {self.price} on {self.date_of_spending}'

    class Meta:
        verbose_name = "Expense"
        verbose_name_plural = "Expenses"
