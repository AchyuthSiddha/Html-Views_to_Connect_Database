from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


from app1.models import *


def Insertion_Topic(request):
    tn=input("enter a Topic name:")
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    return HttpResponse("inserted data on topic")


def Insertion_Webpage(request):
    tn=input('input enter a topic name:')
    na=input("enter a name:")
    ur=input("enter a url:")
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    wo=Webpage.objects.get_or_create(topic_name=TO,name=na,url=ur)[0]
    wo.save()
    return HttpResponse("inserted data into webpage:")

def Insertion_AccessRecord(request):
    tn=input('input enter a topic name:')
    na=input("enter a name:")
    ur=input("enter a url:")
    auth=input("enter a author name:")
    data=input("enter a date:")
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    wo=Webpage.objects.get_or_create(topic_name=TO,name=na,url=ur)[0]
    wo.save()
    ao=AccessRecord.objects.get_or_create(name=wo,author=auth,date=data)[0]
    ao.save()
    return HttpResponse("data inserted into access Records:")

def Display_Topic(request):
    LOT=Topic.objects.all()
    d={'topics':LOT}
    return render(request,'Display_Topic.html',d)

def Display_Webpage(request):
    WOT=Webpage.objects.all()
    d={'webpage':WOT}
    return render(request,'Display_Webpage.html',d)

def Access_Record(request):
    AOT=AccessRecord.objects.all()
    d={'access':AOT}
    return render(request,'Access_Record.html',d)