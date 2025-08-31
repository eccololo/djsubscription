from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings

from writer.models import Article
from .models import Subscription

from account.models import CustomUser


@login_required(login_url="my-login")
def client_dashboard(request):

    try:

        subDetails = Subscription.objects.get(user=request.user)

        subscription_plan = subDetails.subscription_plan

        context = {
            "SubPlan": subscription_plan
        }

        return render(request, "client/client-dashboard.html", context)
    
    except:

        subscription_plan = "None"

        context = {
            "SubPlan": subscription_plan
        }

        return render(request, "client/client-dashboard.html", context)
    



@login_required(login_url="my-login")
def browse_articles(request):

    try:

        subDetail = Subscription.objects.get(user=request.user, is_active=True)
    
    except:

        return render(request, "client/subscription-locked.html")
    
    current_subscription_plan = subDetail.subscription_plan

    if current_subscription_plan == "Standard":

        articles = Article.objects.all().filter(is_premium=False)

    elif current_subscription_plan == "Premium":

        articles = Article.objects.all()

    context = {
        "AllClientsArticles": articles
    }

    return render(request, "client/browse-articles.html", context)


@login_required(login_url="my-login")
def subscription_locked(request):

    return render(request, "client/subscription-locked.html")



@login_required(login_url="my-login")
def subscription_plans(request):

    context = {
        "PayPalClientID": settings.PAYPAL_CLIENT_ID
    }

    return render(request, "client/subscription-plans.html", context)


@login_required(login_url="my-login")
def account_management(request):

    return render(request, "client/account-management.html")


@login_required(login_url="my-login")
def create_subscription(request, subID, plan):

    custom_user = CustomUser.objects.get(email=request.user)

    firstName = custom_user.first_name
    lastName = custom_user.last_name

    fullName = firstName + " " + lastName

    selected_sub_plan = plan

    if selected_sub_plan == "Standard":

        sub_cost = "4.99"

    elif selected_sub_plan == "Premium":

        sub_cost = "9.99"

    subscription = Subscription.objects.create(
        subscriber_name = fullName,
        subscription_plan = selected_sub_plan,
        subscription_cost = sub_cost,
        paypal_subscription_id = subID,
        is_active = True,
        user = request.user
    )

    context = {
        "SubscriptionPlan": selected_sub_plan
    }

    return render(request, "client/create-subscription.html")
