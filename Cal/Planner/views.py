from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponseRedirect, JsonResponse
from django.http.response import HttpResponse
from django.urls import reverse
from .forms import NewItemForm, UploadCalendarForm
from .models import User, Item
from ics import Calendar
from .utils import addEvent, assignEvent, icaltojson
import mimetypes
from django.core.files import File
from datetime import datetime
import os.path
# Create your views here.

def index(request):
    user_id=request.user.id
    more_events=None
    events=None
    disable_download=True
    if user_id is not None:
        events=Item.objects.filter(user_id=user_id, assigned=False)
        if not events.exists():
            events=None
        if request.user.cal:
            more_events,_=icaltojson(request.user.cal.path)
        filename=str(request.user.id)+".ics"
        if os.path.exists(filename):
            disable_download=False
    return render(request, "Planner/index.html", {"Events":events, "Cal":more_events, "disable_download":disable_download})

@login_required
def add(request):
    if request.method=="POST":
        item=NewItemForm(request.POST)
        if item.is_valid():
            item=item.save(commit=False)
            item.user_id=request.user
            item.save()
        else:
            return render(request, "Planner/add.html", {"form":item, "message":item.errors})
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
        email=request.POST["email"]
        password=request.POST["password"]
        confirm_password=request.POST["confirm-password"]
        if password!=confirm_password:
            return render(request, "Planner/register.html", {
                "message":"Password and Confirm Password do not match"
            })
        try:
            user=User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "Planner/register.html", {
                "message":"Username already taken"
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "Planner/register.html")

@login_required
def assign(request):
    unassigned=[]
    cal=Calendar()
    new_cal=Calendar()
    events=[]
    if request.user.cal!="":
        events, cal=icaltojson(request.user.cal.path)
    items=Item.objects.filter(user_id=request.user.id, assigned=False).order_by("-priority","duration")
    for item in items:
        s_t=assignEvent(events, item)
        if s_t is not None:
            cal=addEvent(cal,item,s_t)
            new_cal=addEvent(new_cal, item, s_t)
            item.assigned=True
            item.early_start_time=s_t.datetime
            item.late_start_time=s_t.datetime
            item.save()
            events=list(cal.events)
        else:
            unassigned.append(item.name)
    user=request.user
    filename="temp.ics"
    with open(filename, 'w') as f:
        f.writelines(cal.serialize_iter())
    user.cal=File(open(filename, 'rb'), name=str(user.id)+".ics")
    user.save()
    filename=str(request.user.id)+".ics"
    with open(filename, 'w') as f:
        f.writelines(new_cal.serialize_iter())
    message=str(len(items)-len(unassigned))+" Events assigned successfully\n" + str(len(unassigned)) +" Events assigned unsuccessfully"
    return render(request, "Planner/assign.html", {"message":message})

@login_required
def download(request):
    filename=str(request.user.id)+".ics"
    path=open(filename, 'r')
    mime_type,_=mimetypes.guess_type(filename)
    response=HttpResponse(path,content_type=mime_type)
    response['Content-Disposition']="attachment; filename=%s" % filename
    return response

@login_required
def upload(request):
    if request.method=="POST":
        user=request.user
        upload=UploadCalendarForm(request.POST, request.FILES)
        if upload.is_valid:
            user.cal=request.FILES["cal"]
            user.save()
            return HttpResponseRedirect(reverse("index"))
    return render(request, "Planner/upload.html", {"form":UploadCalendarForm()})

@login_required
def edit(request, id):
    event=Item.objects.filter(id=id)[0]
    if event.user_id!=request.user:
        return
    item=NewItemForm(data={"name":event.name,"early_start_time_0":event.early_start_time.date(),"early_start_time_1":event.early_start_time.time(),"late_start_time_0":event.late_start_time.date(),"late_start_time_1":event.late_start_time.time(),"duration":event.duration,"priority":event.priority})
    if request.method=="POST":
        item=NewItemForm(request.POST)
        if item.is_valid():
            item=item.save(commit=False)
            event.name=item.name
            event.early_start_time=item.early_start_time
            event.late_start_time=item.late_start_time
            event.duration=item.duration
            event.priority=item.priority
            event.save()
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "Planner/edit.html", {"form":item, "id":id, "message":item.errors})
    else:
        return render(request, "Planner/edit.html", {"form":item, "id":id})
