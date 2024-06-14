from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, TemplateView, UpdateView, CreateView
from core.forms import ExpenseForm, ProfileEditForm
from core.models import Account, Expense
import json
from django.db.models import Q
from core.utils import get_currency_info


class HomeView(TemplateView):
    template_name = 'main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


class ExpensesListView(LoginRequiredMixin, ListView):
    model = Expense
    template_name = 'expenses_list.html'
    context_object_name = 'expenses'

    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)


class ExpenseSearchView(LoginRequiredMixin, ListView):
    model = Expense
    template_name = 'expenses_list.html'
    context_object_name = 'expenses'

    def get_queryset(self):
        queryset = Expense.objects.filter(user=self.request.user)
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(Q(description__icontains=query))
        return queryset


class EditProfileView(LoginRequiredMixin, UpdateView):
    model = Account
    template_name = 'edit_profile.html'
    form_class = ProfileEditForm
    success_url = '/profile/'

    def get_object(self, queryset=None):
        return self.request.user.account

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        account = get_object_or_404(Account, user=self.request.user)

        expenses = Expense.objects.filter(user=self.request.user)

        expense_data = {}
        for expense in expenses:
            month_year = expense.date_of_spending.strftime('%Y-%m')
            if month_year in expense_data:
                expense_data[month_year] += float(expense.price)
            else:
                expense_data[month_year] = float(expense.price)

        sorted_expense_data = sorted(expense_data.items())

        labels = [data[0] for data in sorted_expense_data]
        data = [data[1] for data in sorted_expense_data]

        expense_data_json = json.dumps({
            'labels': labels,
            'data': data,
        })

        local_currency, local_currency_symbol = get_currency_info(self.request)

        context['account'] = account
        context['expense_data_json'] = expense_data_json
        context['local_currency'] = local_currency
        context['local_currency_symbol'] = local_currency_symbol

        return context


class ExpenseCreateView(LoginRequiredMixin, CreateView):
    model = Expense
    form_class = ExpenseForm
    template_name = 'expense_create.html'
    success_url = '/profile/'  # Adjust the URL to redirect after successful form submission

    def form_valid(self, form):
        expense = form.save(commit=False)
        expense.user = self.request.user
        expense.save()

        try:
            account = Account.objects.get(user=self.request.user)
            account.balance -= expense.price
            account.save()
        except Account.DoesNotExist:
            pass

        return super().form_valid(form)
