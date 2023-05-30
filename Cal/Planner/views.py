from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import NewItemForm
from .models import User, Item
# Create your views here.

def index(request):
    user_id=request.user.id
    events=[]
    if user_id is not None:
        events=Item.objects.filter(user_id=user_id)
    return render(request, "Planner/index.html", {"Events":events})

@login_required
def add(request):
    if request.method=="POST":
        item=NewItemForm(request.POST)
        if item.is_valid():
            item=item.save(commit=False)
            item.user_id=request.user
            item.save()
    return render(request, "Planner/add.html", {"form":NewItemForm()})

def login_view(request):
    if request.method=="POST":
        user=authenticate(request, username=request.POST["username"], password=request.POST["password"])
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "Planner/login.html", {
                "message":"Invalid Credentials"
            })
    else:
        return render(request, "Planner/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        try:
            user=User.objects.create_user(username, username, password)
            user.save()
        except IntegrityError:
            return render(request, "Planner/register.html", {
                "message":"Username already taken"
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "Planner/register.html")