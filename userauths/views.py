from django.shortcuts import render, redirect
from userauths.forms import UserRegisterForm
from userauths.models import Profile

from django.contrib import messages
from django.contrib.auth import authenticate, login

# Create your views here.

def RegisterView(request):
    if request.user.is_authenticated:
        messages.warning(request, "You are registered!")
        return redirect("core:feed")

    form = UserRegisterForm(request.POST or None)
    if form.is_valid(): #waliduje informacje pod względem ataków
        form.save()
        full_name = form.cleaned_data.get("full name")
        phone = form.cleaned_data.get("phone")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password1")

        user = authenticate(email = email, password = password)
        login(request, user)

        messages.success(request, f"Hi {full_name}. your account was created succesfully!")

        profile = Profile.objects.get(user=request.user)#tak jakby był tu przypisany id z Usera
        profile.full_name = full_name
        profile.phone = phone
        profile.gender = gender
        profile.save()

        messages.success(request, f"Hi {full_name}. your account was created succesfully!")
        return redirect("core:feed")
    
    context = {
        "form":form
    }
    return render(request, "userauths/sign-up.html", context)