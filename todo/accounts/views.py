from django.shortcuts import render, redirect
from .froms import CreatingUserForm
from django.contrib.auth.models import User
from django.contrib.messages import error
from django.http import HttpResponse
from .models import Profile
from django.contrib.auth import login, logout, authenticate
import os
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
# Create your views here.


def register(request):
    if request.method == "POST":
        form = CreatingUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/accounts/login/")
        else:
            context = {
            "form" : CreatingUserForm(),
            "message":[form.error_messages,form.is_valid()],
            "post": request.POST
            }
            return render(request, "registration/register.html", context)
    else:
        context = {
            "form" : CreatingUserForm()
        }
        return render(request, "registration/register.html", context)

    

def login_user(request):
    logout(request)
    if request.method == "POST":
        user = authenticate(username=request.POST["username"], password=request.POST["password"])
        if user is not None:
            login(request,user)
            return redirect("/")
    return render(request, "registration/login.html", {})




def profile(request):
    if request.method == "POST":
        user = request.user
        user.username = request.POST["username"]
        user.email = request.POST["email"]
        user.save()
        if request.FILES:
            profile = Profile.objects.get(user_id = user.id)
            if user.profile.img.url != "/media/profiles/Default.jpg":
                os.remove("media/"+user.profile.img.__str__())
            profile.delete()
            profile = Profile(user=user, img=request.FILES["pic"])
            profile.save()
        return redirect("/accounts/profile/")

    if request.user.is_authenticated:
        context={
            "user":request.user,
            "profile_pic":request.user.profile.img.url,
        }
        return render(request, "registration/profile.html",context)
    return render(request, "registration/profile.html",{})

