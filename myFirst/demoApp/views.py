from django.shortcuts import render
from django.http import HttpResponse


def home(request):

  person={
    'name':"Niharika",
    'age':20,
    'Occupation':"student",
     'course':["Java","C","Python","HTML"]

  }
  return render(request,'index.html',context=person)
  


def page_Success(request):
  return HttpResponse("<h1> This is a success page developed by Niharika</h1>")

def page_details(request,courseid):
  data={
    '1':"java",
    '2':"Python"
  }
  return render(request,"coursedetails.html",context=data)

def details(request,courseid):
   return HttpResponse(courseid)