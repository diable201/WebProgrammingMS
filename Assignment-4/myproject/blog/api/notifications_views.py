from django.shortcuts import render

def notifications_view(request):
    return render(request, "blog/notifications.html")


def login_view(request):
    return render(request, "blog/login.html")
