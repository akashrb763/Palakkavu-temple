from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import Feeds, Notifications,AnnounceMent,PoojaTime
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from .models import Enquiry


# Create your views here.
def index(request):
    # feed_list = Feeds.objects.all()
    feed_list= Feeds.objects.all().order_by('-id')
    gall = Notifications.objects.all()
    tim=PoojaTime.objects.all()
    anno=AnnounceMent.objects.all()

    paginator=Paginator(feed_list,8)
    try:
        page=int(request.GET.get('page',1))
    except:
        page=1

    try:
       feeds=paginator.page(page)

    except (EmptyPage,InvalidPage):
        feeds=paginator.page(paginator.num_pages)



    return render(request, "index.html", {'im': gall,'time':tim,'annons':anno,'feeds':feeds})
    # return HttpResponse("hello")

def members(request):

    return render(request,"members.html")


def details(request,feeds_id):
    feeds=Feeds.objects.get(id=feeds_id)
    return render(request,"details.html",{'feeds':feeds})


def about(request):

    return render(request,"about.html")

def donate(request):


    return render(request,"contribution.html")

def enquiry(request):
    if request.method=="POST":
        name=request.POST.get('name')
        number=request.POST.get('mobile_number')
        qury=request.POST.get('qury')
        data=Enquiry(name=name,mobile_no=number,qury=qury)
        data.save()
    return render(request,"enquiry.html")

def notification(request,notify_id):
    ttl=Notifications.objects.get(id=notify_id)

    return render(request,"notifydetails.html",{"ttl":ttl})

def todaypooja(request):
    today=PoojaTime.objects.all()

    return render(request,"todaypooja.html",{"today":today})


def spcilepooja(request):

    return render(request,"spcilepooja.html")

def login(request):

    return render(request,"login.html")


def login(request):

    return  redirect('/admin')
    # if request.method== 'POST':
    #     username=request.POST['username']
    #     password=request.POST['password']
    #     user=auth.authenticate(username=username,password=password)
    #
    #     if user is not None:
    #        auth.login(request,user)
    #        return  redirect('/admin')
    #     else:
    #         messages.info(request,'Invalid Credentials')
    #         return redirect('../login')
    # return render(request,"login.html")


def logout(request):
    auth.logout(request)
    return redirect('/')