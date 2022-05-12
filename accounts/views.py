from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
# from .models import Reporter, Investigator
from django.contrib import messages
from random import randint

def register(request):   
    if request.method == "POST" :
        firstname = request.POST['f_name']
        lastname = request.POST['l_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password : 
            if User.objects.filter(username = username).exists():
                messages.info(request, "Username already taken")
                return redirect("register")
            elif User.objects.filter(email = email).exists():
                messages.info(request, "Email already in use")
                return redirect("register")
            else :
                user = User.objects.create_user(username, email, password)
                user.first_name, user.last_name = firstname, lastname
                user.save()
                auth.login(request, user)
                return redirect("/main/")
        else :
            messages.info(request, 'Password not matched!')
            return redirect("register")
    return render(request, "accounts/register.html")


def registerAsInvestigator(request):
    # if request.method == "POST" :
    #     investigator_id = 'INV_' + chr(randint(65,70)) + str(randint(100000,999999))  # Generating an ID for the investigator
    #     firstname = request.POST['f_name']
    #     lastname = request.POST['l_name']
    #     fullname = firstname + ' ' + lastname
    #     phone= request.POST['phone']
    #     email = request.POST['email']
    #     username = request.POST['username']
    #     password = request.POST['password']
    #     confirm_password = request.POST['confirm_password']
    #     if password == confirm_password : 
    #         if User.objects.filter(username = username).exists():
    #             messages.info(request, "Username already taken")
    #             return redirect("register")
    #         elif User.objects.filter(email = email).exists():
    #             messages.info(request, "Email already in use")
    #             return redirect("register")
    #         else :
    #             user = User.objects.create_user(username, email, password, first_name=firstname, last_name=lastname)
    #             user.save()
    #             investigator = Investigator(investigator_id=investigator_id, name=fullname, phone=phone, email=email, cases="will be declared soon")
    #             investigator.save()
    #             auth.login(request, user)
    #             return redirect("/main/")
    #     else :
    #         messages.info(request, 'Password not matched!')
    #         return redirect("register")
    # return render(request, 'accounts/registerAsInvestigator.html')
    pass



def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user:
            auth.login(request, user)
            return redirect("/main/")
        else:           
            return render(request, "accounts/login.html")
    return render(request, "accounts/login.html")


def loginAsInvestigator(request):
    # if request.method == "POST":
    #     username = request.POST['username']
    #     password = request.POST['password']
    #     user = auth.authenticate(request, username=username, password=password)
    #     if user:
    #         auth.login(request, user)
    #         return redirect("/main/")
    #     else:    
    #         messages.info(request, "Please enter valid username and password")       
    #         return render(request, "accounts/loginAsInvestigator.html")
    # return render(request, "accounts/loginAsInvestigator.html")
    pass


def logout(request):
    auth.logout(request)
    return redirect("/main/")
