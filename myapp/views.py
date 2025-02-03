from django.shortcuts import render,redirect,get_object_or_404
from .models import Data
from django.contrib import messages
from .form import ContactForm

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

def delete(request,id):
    a = Data.objects.get(id=id)
    a.delete()
    return redirect("show")

def update_contact(request, id):
    b = get_object_or_404(Data, id=id)
    
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=b)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ContactForm(instance=b)
        
    return render(request,'updatecontact.html',{'form':form})
        
    
    
    