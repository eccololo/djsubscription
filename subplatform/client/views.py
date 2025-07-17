from django.shortcuts import render



def client_dashboard(request):

    context = {

    }

    return render(request, "client/client-dashboard.html")
