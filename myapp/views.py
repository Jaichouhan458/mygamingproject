from django.shortcuts import render,redirect,HttpResponse
from .models import Data
from django.contrib import messages 

# Create your views here.

def homepage(request):
    return render(request,'home.html')

def shop(request):
    return render(request,'shop.html')

def product(request):
    return render(request,'product.html')

def contact(request):
    return render(request,'contact.html')

def signin(request):
    return render(request,'signin.html')

def save(request):
    return render(request,'save.html')

from django.shortcuts import render, redirect
from django.contrib import messages  # Import messages framework
from .models import Data  # Import your Data model

def contact_data(request):
    if request.method == "POST":
        name = request.POST.get('name')
        last = request.POST.get('last_name')
        email = request.POST.get('email')
        msg = request.POST.get('message')
        sub = request.POST.get('subject')

        # Save data using create()
        # Data.objects.create(
        #     name=name,
        #     lastname=last,
        #     email=email,
        #     message=msg,
        #     subject=sub
        # )
        d = Data (
             name=name,
            lastname=last,
            email=email,
            message=msg,
            subject=sub
        )
        d.save()
     
        messages.success(request, "Your message has been sent successfully!")  # Success message
        
        return redirect("show")  # Redirect to the "show" view (make sure the URL name is correct)
    
    return render(request, "contact.html")




def show_data(request):
    data  = Data.objects.all()
    
    return render(request,'showData.html',{'data':data})