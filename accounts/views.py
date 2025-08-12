from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Account
from .forms import TransactionForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
         user = form.save()
        Account.objects.create(user=user)  # ✅ Create account immediately
        login(request, user)
        return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def dashboard(request):
    account = Account.objects.get(user=request.user)
    return render(request, 'dashboard.html', {'account': account})

@login_required
def deposit(request):
    account = Account.objects.get(user=request.user)
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            account.balance += form.cleaned_data['amount']
            account.save()
            return redirect('dashboard')
    else:
        form = TransactionForm()
    return render(request, 'transaction.html', {'form': form, 'title': 'Deposit'})

@login_required
def withdraw(request):
    account = Account.objects.get(user=request.user)
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            if account.balance >= amount:
                account.balance -= amount
                account.save()
            return redirect('dashboard')
    else:
        form = TransactionForm()
    return render(request, 'transaction.html', {'form': form, 'title': 'Withdraw'})
