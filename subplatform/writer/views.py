from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url="my-login")
def writer_dashboard(request):

    context = {

    }

    return render(request, "writer/writer-dashboard.html")

