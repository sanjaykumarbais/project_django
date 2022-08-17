from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Emp_mng,Testimonial
from .form import FeedbackForm,Emp_mngForm
# Create your views here.
def emp_mng_home(request):

    emps=Emp_mng.objects.all()
    return render(request, "emp_mng/home.html",{
        'emps':emps
    })

def add_emp_mng(request):
    if request.method=="POST":
        #data fetch
        emp_name=request.POST.get("emp_name")
        emp_id=request.POST.get("emp_id")
        emp_address=request.POST.get("emp_address")
        emp_phone=request.POST.get("emp_phone")
        emp_working=request.POST.get("emp_working")
        emp_department=request.POST.get("emp_department")

        #create model object and set the data
        e=Emp_mng()
        e.name=emp_name
        e.emp_id=emp_id
        e.phone=emp_phone
        e.address=emp_address
        e.department=emp_department
        if emp_working is None:
            e.working=False
        else:
            e.working=True

        #save the object
        e.save()

        #prepare message




        return redirect("/emp_mng/home/")
    form=Emp_mngForm()
    
    return render(request, "emp_mng/add_emp_mng.html",{'form':form})

def delete_emp_mng(request,emp_id):
    emp_mng=Emp_mng.objects.get(pk=emp_id)
    emp_mng.delete()
    return redirect("/emp_mng/home/")


def update_emp_mng(request,emp_id):
    emp_mng=Emp_mng.objects.get(pk=emp_id)
    return render(request,"emp_mng/update_emp_mng.html",{
        'emp_mng':emp_mng
    })

def do_update_emp_mng(request,emp_id):
    if request.method=='POST':
        emp_name=request.POST.get("emp_name")
        emp_id_temp=request.POST.get("emp_id")
        emp_address=request.POST.get("emp_address")
        emp_phone=request.POST.get("emp_phone")
        emp_working=request.POST.get("emp_working")
        emp_department=request.POST.get("emp_department")

        e=Emp_mng.objects.get(pk=emp_id)
        e.name=emp_name
        e.emp_id=emp_id_temp
        e.phone=emp_phone
        e.address=emp_address
        e.department=emp_department
        if emp_working is None:
            e.working=False
        else:
            e.working=True

        e.save()

    return redirect("/emp_mng/home/")

def testimonials(request):
    testi=Testimonial.objects.all()


    return render(request,"emp_mng/testimonials.html",{
        'testi':testi
    })


def feedback(request):
    if request.method=='POST':
        form=FeedbackForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['email'])
            print(form.cleaned_data['name'])
            print(form.cleaned_data['feedback'])
            print("data saved")
        else:
            return render(request, "emp_mng/feedback.html",{'form':form})

    else:
        form=FeedbackForm()

        return render(request, "emp_mng/feedback.html",{'form':form})