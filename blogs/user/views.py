from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

def userregisterform(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the new user
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account created for {username}!")
            login(request, user)  # Log the user in after registration
            return redirect("blog_list")  # Redirect to home page (change as needed)
    else:
        form = UserCreationForm()

    return render(request, "user/register.html", {"form": form})


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome, {username}!")
                return redirect("blog_list")  # Redirect to home page (change as needed)
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid form submission.")
    
    form = AuthenticationForm()
    return render(request, "user/login.html", {"form": form})

def user_logout(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect("login")  # Redirect to login page

