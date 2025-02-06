from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User  # Ensure using Django's User model
from .models import Data, User_Info  # Ensure models are correctly imported
from .form import ContactForm, UserSignUp

# Create your views here.
def homepage(request):
    return render(request, 'home.html')

def shop(request):
    return render(request, 'shop.html')

def product(request):
    return render(request, 'product.html')

def contact(request):
    return render(request, 'contact.html')

def signin(request):
    return render(request, 'signin.html')

def save(request):
    return render(request, 'save.html')

# ✅ Corrected Contact Form Data Save
def contact_data(request):
    if request.method == "POST":
        name = request.POST.get('name')
        last = request.POST.get('last_name')
        email = request.POST.get('email')
        msg = request.POST.get('message')
        sub = request.POST.get('subject')

        d = Data(
            name=name,
            lastname=last,
            email=email,
            message=msg,
            subject=sub
        )
        d.save()
     
        messages.success(request, "Your message has been sent successfully!")  
        return redirect("show")  
    
    return render(request, "contact.html")

# ✅ Show Data View (Currently Redirecting to Home)
def show_data(request):
    return render(request, 'home.html')

# ✅ Delete Data Entry
# def delete(request, id):
#     a = get_object_or_404(Data, id=id)
#     a.delete()
#     return redirect("show")

# ✅ Update Contact Data
# def update_contact(request, id):
#     b = get_object_or_404(Data, id=id)
    
#     if request.method == 'POST':
#         form = ContactForm(request.POST, instance=b)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#     else:
#         form = ContactForm(instance=b)
        
#     return render(request, 'updatecontact.html', {'form': form})


# ✅ Fixed SignUp Form Handling
def signup_form(request):
    if request.method == "POST":
        form = UserSignUp(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('login')  # Redirect to login page
    else:
        form = UserSignUp()

    return render(request, "signup.html", {"form": form})


# ✅ Fixed Login Function
def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            user = User_Info.objects.get(username=username)  # Fetch user by username
            if user.Password == password:  # Direct comparison (plaintext)
                request.session["user_id"] = user.id  # Store user in session
                request.session['user_name'] = user.username
                messages.success(request,{user.username})
                
                
                return redirect("/")  # Redirect to homepage after successful login
            else:
                messages.error(request, "Invalid username or password.")
        except User_Info.DoesNotExist:
            messages.error(request, "User not found.")

    return render(request, "signin.html")
