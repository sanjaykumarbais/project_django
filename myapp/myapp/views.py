from django.http import HttpResponse
from django.shortcuts import render

import datetime
def home(request):
    date = datetime.datetime.now()
    isActive=True
    name="sanjay"
    list_of_programs=[
        'WAP to check even or odd',
        'WAP to check prime number',
        'WAP to print all prime number from 1 to 100',
        'WAP to print pascals triangle'
    ]
    student={
        'student_name':"Rahul",
        'student_collage':"zyx",
        'student_city':"locknow"
    }
    data={
        'date':date,
        'isActive':isActive,
        'name':name,
        'list_of_programs':list_of_programs,
        'student_data':student
    }
    #return HttpResponse("<h1>Hello this is index page </h1> "+str(date))
    return render(request, "home.html",data)

def about(request):
    #return HttpResponse("<h1>this is about page </h1>")
    return render(request, "about.html",{})

def services(request):
    #return HttpResponse("<h1>this is services about page </h1>")
    return render(request, "services.html",{})
