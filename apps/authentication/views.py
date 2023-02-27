# -*- encoding: utf-8 -*-


# Create your views here.
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm, SignUpForm, deposit_form
from .models import deposit
from django.contrib.auth.decorators import login_required


def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/dashboard.html")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Oops, that’s not right, try again'

    return render(request, "accounts/login.html", {"form": form, "msg": msg})


def register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'User created - please <a href="{% login %}">login</a>.'
            success = True

            return render(request, 'accounts/register_done.html')

        else:
            msg = 'Oops, that’s not right, try again'
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})

def register_done(request):
    return render(request, 'accounts/register_done.html')

@login_required
def deposit_view(request):
    add = None
    success = False

    if request.method == 'POST':
        form = deposit_form(request.POST)
        if form.is_valid():
            token = form.cleaned_data.get("token")
            amount = form.cleaned_data.get("amount")
            plan = form.cleaned_data.get("plan")
            order_id = form.cleaned_data.get("order_id")
            payment = deposit(token=token, plan=plan, amount=amount)
            payment.save()

            success = True

            if token == "BTC":
                add = "bitcoinaddress"

            elif token == "ETH":
                add = "ethaddress"

            elif token == "USDT":
                add = "tetheraddress"

            return render(request, 'accounts/deposit_confirm.html')

    else:
        form = deposit_form()
    return render(request, "accounts/deposit.html", {"form": form, "add": add, "success": success})