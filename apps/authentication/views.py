# -*- encoding: utf-8 -*-


# Create your views here.
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm, SignUpForm, deposit_form
from .models import deposit, variables
from django.contrib.auth.decorators import login_required
from django.template import loader


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
            payment = deposit(token=token, plan=plan, amount=amount)
            payment.save()

            objs = deposit.objects.all()
            objs = deposit.objects.filter(plan=plan, amount=amount, token=token)


            success = True
            variables_instance = variables.objects.first()

            if payment.token == 'BTC':
                add = variables_instance.BTC
            elif payment.token == 'ETH':
                add = variables_instance.ETH
            elif payment.token == 'USDT':
                add = variables_instance.USDT

            return render(request, 'accounts/deposit_confirm.html', {"add": add, "objs":objs})

    else:
        form = deposit_form()
    return render(request, "accounts/deposit.html", {"form": form, "success": success})


def about(request):
    return render(request,"accounts/about.html")

from datetime import date, timedelta
from .models import others

def increase_field():
    # Get today's date and the model object you want to update
    today = date.today()
    obj = others.objects.get(id=1)

    # Check if the date has changed since the last update
    if today != obj.last_update:
        # Update the field and save the object
        obj.total_orders += 1
        obj.last_update = today
        obj.save()
