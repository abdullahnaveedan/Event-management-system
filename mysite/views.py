from django.http import HttpResponse, HttpResponseRedirect  
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth.models import User
from polls.models import *
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from datetime import datetime

def index(request):
    print(request.user.username)
    return render(request , "user/index.html")

def events(request):
    data = registeredevents.objects.all()
    context = {
        'data' : data
    }
    if request.method == "POST":
        evid = request.POST.get('eveid')
        registrar = request.user.username
        user = registeredevents.objects.get(eventid = evid)
        registered = user.username
        notification(description = f"{registrar} registered in your event.",username=registered).save()
        notification(description = f"You Sucessfully  Registered in {user.eventname} event.",username=registrar).save()

    return render(request , "user/allevents.html",context)
    
def notifications(request):
    data = notification.objects.filter(username=request.user.username)
    formatted_datetimes = [entry.datetime.strftime('%Y-%m-%d %I:%M:%S %p') for entry in data]

    descriptions = [entry.description for entry in data]
    dates = formatted_datetimes

    zipped_data = zip(descriptions, dates)

    context = {
        'zipped_data': zipped_data
    }

    return render(request, "user/notification.html", context)


      
def signin(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            auth_login(request, user)
            print("login Sucessfully")
            return redirect("home")
        else:
            print("incorrect Cridentials")

    return render(request , "user/login.html")
    
def signup(request):
    if request.method == "POST":
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']
        if password == confirmpassword:
            firstname = request.POST['firstname']
            lastname = request.POST['lastname']
            username = request.POST['username']
            email = request.POST['email']
            user = User.objects.create_user(username, email, password)
            user.first_name = firstname
            user.last_name = lastname
            user.save()
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
            notification(description = f"Welcome {firstname}!",username=username).save()
            return render(request,"user/index.html")
        else:
            return HttpResponse("<h1>Password is not same</h1>")

    return render(request , "user/signup.html")
    
def thanks(request):
    return render(request , "user/thanks.html")
    
def contactus(request):
    if request.method == "POST":
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        usermails(email = email, subject = subject, message = message).save()
        if request.user.is_authenticated:
            notification(description = "We have received your message.We will get back soon.",username=username).save()
        return render(request,"user/thanks.html")
    return render(request , "user/contact.html")
    
def myevents(request):
    data = registeredevents.objects.filter(username = request.user.username)
    context={
        'data' : data
    }
    if request.method == "POST":
        eventname = request.POST['eventname']  
        purpose = request.POST['purpose'] 
        location = request.POST['location'] 
        date = request.POST['date'] 
        typeofevent = request.POST['typeofevent'] 
        # document = request.POST['document'] 
        username = request.user.username
        registeredevents(eventname = eventname, purpose = purpose,location = location, date = date, type = typeofevent,username = username).save()

        notification(description = "Your Event is Registered",username=username).save()
        return render(request,"user/thanks.html")
    return render(request,"user/myevents.html",context)

def signout(request):
    auth_logout(request)
    print("Logout Sucessfully")
    return redirect("home")

def deleteevent(request,myid):
    event = registeredevents.objects.get(eventid=myid)
    notification(description = f"Your event {event.eventname} is Deleted.",username = request.user.username).save()
    event.delete()
    return redirect("myevents")