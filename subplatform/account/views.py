from django.shortcuts import render


def home(request):

    context = {

    }

    return render(request, "account/index.html", context)


def register(request):

    context = {

    }

    return render(request, "account/register.html", context)


def my_login(request):

    context = {

    }

    return render(request, "account/my-login.html", context)
