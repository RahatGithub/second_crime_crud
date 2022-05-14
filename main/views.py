from django.shortcuts import render, redirect
from .models import Case, Contact
from .forms import ReportCase, UpdateCase, RegisterInvestigator, ContactMsg
from accounts.models import Reporter, Investigator
from django.contrib.auth.models import User, auth
from random import randint
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'main/index.html')


def reportCrime(request):
    if request.method == "POST":
        user = request.user
        case_code = 'CAS_' + chr(randint(65,70)) + str(randint(100000,999999))  # Generating a code for the case
        location = request.POST.get('location', '')
        desc = request.POST.get('desc', '')
        fullname = user.first_name + ' ' + user.last_name
        phone = request.POST.get('phone', '')
        email = user.email 
        case = Case(case_code=case_code, location=location, desc=desc, status="Pending", reporter_name=fullname, reporter_phone=phone, investigator_code="NA")
        case.save()
        reporter = Reporter.objects.filter(email=email)
        if reporter: 
            # add this case to the reporter's reports
            pass
        else:
            reporter_code = 'REP_' + chr(randint(65,70)) + str(randint(100000,999999))  # Generating a code for the reporter
            new_reporter = Reporter(reporter_code=reporter_code, name=fullname, phone=phone, email=email, cases="will be shown later")
            new_reporter.save()
    return render(request, 'main/reportCrime.html')


def dashboard(request, username):
    if request.method == 'POST':
        fm = ReportCase(request.POST)   
        if fm.is_valid():
            case_code = 'CAS_' + chr(randint(65,70)) + str(randint(100000,999999))  # Generating a code for the case
            user = request.user 
            fullname = user.first_name + ' ' + user.last_name
            desc = fm.cleaned_data['desc']
            location = fm.cleaned_data['location']
            reporter_phone = fm.cleaned_data['reporter_phone']
            record = Case(case_code=case_code, location=location, desc=desc, status="Pending", reporter_name=fullname, reporter_phone=reporter_phone, investigator_code="NA")
            record.save() 
            fm = ReportCase()
    else:
        fm = ReportCase()
    
    user = request.user
    email = user.email
    fullname = user.first_name + ' ' + user.last_name
    cases, userRole = None, None 
    if Case.objects.filter(reporter_name=fullname).exists(): 
        cases = Case.objects.filter(reporter_name=fullname)
        userRole = "reporter" 
    elif Case.objects.filter(investigator_code=fullname).exists():
        cases = Case.objects.filter(investigator=fullname)
        userRole = "investigator"
    else: 
        pass
    params = {'username':username, 'fullname':fullname, 'cases':cases, 'userRole':userRole, 'form':fm}
    return render(request, 'main/dashboard.html', params)


def updateData(request, id):
    if request.method== 'POST':
        record = Case.objects.get(pk=id)
        fm = ReportCase(request.POST, instance=record) # Generating a form with the values of the record with the given id
        if fm.is_valid():
            fm.save()
    else:
        record = Case.objects.get(pk=id)
        fm = ReportCase(instance=record) 
    return render(request, 'main/updateData.html', {'form':fm})


def deleteData(request, id):
    if request.method == 'POST':
        record = Case.objects.get(pk=id) 
        username = request.user.username
        record.delete()
        return redirect('/main/dashboard/'+username)


def adminPanel(request):
    if request.method == 'POST':
        fm = RegisterInvestigator(request.POST)   
        if fm.is_valid():
            investigator_code = 'INV_' + chr(randint(65,70)) + str(randint(100000,999999))  # Generating a code for the investigator
            name = fm.cleaned_data['name']
            phone = fm.cleaned_data['phone']
            email = fm.cleaned_data['email']
            record = Investigator(investigator_code=investigator_code, name=name, phone=phone, email=email, cases="")
            record.save() 
            fm = RegisterInvestigator()
    else:
        fm = RegisterInvestigator()
    cases = Case.objects.all()
    reporters = Reporter.objects.all()
    investigators = Investigator.objects.all()
    contacts = Contact.objects.all()
    params = {'form':fm, 'investigators':investigators, 'cases':cases, 'reporters':reporters, 'contacts':contacts}
    return render(request, 'main/adminPanel.html', params)


def updateInvestigator(request, id):
    if request.method== 'POST':
        record = Investigator.objects.get(pk=id)
        fm = RegisterInvestigator(request.POST, instance=record) # Generating a form with the values of the record with the given id
        if fm.is_valid():
            fm.save()
    else:
        record = Investigator.objects.get(pk=id)
        fm = RegisterInvestigator(instance=record) 
    return render(request, 'main/updateInvestigator.html', {'form':fm})


def deleteInvestigator(request, id):
    if request.method == 'POST':
        record = Investigator.objects.get(pk=id) 
        record.delete()
        return redirect('/main/adminPanel/')


def updateCase(request, id):
    if request.method== 'POST':
        record = Case.objects.get(pk=id)
        fm = UpdateCase(request.POST, instance=record) # Generating a form with the values of the record with the given id
        if fm.is_valid():
            fm.save()
    else:
        record = Case.objects.get(pk=id)
        fm = UpdateCase(instance=record) 
    return render(request, 'main/updateCase.html', {'form':fm})

def deleteCase(request, id):
    if request.method == 'POST':
        record = Case.objects.get(pk=id) 
        record.delete()
        return redirect('/main/adminPanel/')


def contact(request):
    if request.method== 'POST':
            # record = Contact.objects.get(pk=id)
            fm = ContactMsg(request.POST)
            if fm.is_valid():
                name = fm.cleaned_data['name']
                phone = fm.cleaned_data['phone']
                message = fm.cleaned_data['message']
                record = Contact(name=name, phone=phone, message=message)
                record.save() 
                fm = ContactMsg()
    else:
        fm = ContactMsg() 
    return render(request, 'main/contact.html', {'form':fm})


def about(request):
    return render(request, 'main/about.html')