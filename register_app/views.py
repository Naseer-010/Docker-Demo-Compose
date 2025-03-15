from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login

# Create your views here.
def home(request):
    return render(request, 'index.html')

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse

def signup(request):
    errors = {}  

    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "")
        confirm_password = request.POST.get("confirm_password", "")

        if not username:
            errors["username"] = "Username is required."
        elif User.objects.filter(username=username).exists():
            errors["username"] = "Username is already registered."    
        
        if not email:
            errors["email"] = "Email is required."
        elif User.objects.filter(email=email).exists():
            errors["email"] = "Email is already registered."

        if not password:
            errors["password"] = "Password is required."
        elif len(password) < 6:
            errors["password"] = "Password must be at least 6 characters long."

        if password != confirm_password:
            errors["confirm_password"] = "Passwords do not match."

        
        if errors:
            return render(request, "index.html", {"errors": errors})

        
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        return HttpResponse("Signup Successful!")  
    return render(request, "index.html")  

def login(request):
    errors = {}

    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "")

        if not username:
            errors["username"] = "Username is required"
        
        if not email:
            errors["email"] = "Email is required"
        if not password:
            errors["password"] = "Password is required"

        if not errors:  
            user = authenticate(username=username, email=email, password=password)
            if user is not None:
                auth_login(request, user)  
                return HttpResponse("<h1>Login Successful!</h1>")  
            else:
                errors["invalid"] = "Wrong email or password"

        return render(request, "index.html", {"errors": errors})
    
    return render(request, "index.html")
