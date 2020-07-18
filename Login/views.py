from django.shortcuts import render,redirect
from Login.models import UserLogin
import json
from django.core.serializers.json import DjangoJSONEncoder
def ShopPage(request):
    name=request.POST.get("email");
    password=request.POST.get("pass");
    print(name);
    print(password)
    values=UserLogin.objects.all();
    for x in values:
        if(x.UserName == name and x.Passwords == password):
            return render(request,"Login/ShopPage.html");
    return render(request,"Login/index.html");

def index(request):
    return render(request,"Login/index.html")

def signup(request):
    return render(request,"Signup/Signup.html")