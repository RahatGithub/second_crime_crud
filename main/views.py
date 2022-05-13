from django.shortcuts import render, redirect
from .models import Case
from accounts.models import Reporter
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
    user = request.user
    email = user.email
    fullname = user.first_name + ' ' + user.last_name
    cases, userRole = None, None 
    if Case.objects.filter(reporter_name=fullname).exists(): 
        cases = Case.objects.filter(reporter_name=fullname)
        userRole = "reporter" 
    elif Case.objects.filter(investigator=fullname).exists():
        cases = Case.objects.filter(investigator=fullname)
        userRole = "investigator"
    else: 
        pass
    params = {'username':username, 'fullname':fullname, 'cases':cases, 'userRole':userRole}
    return render(request, 'main/dashboard.html', params)


def adminPanel(request, username):
    user = request.user
    email = user.email
    fullname = user.first_name + ' ' + user.last_name
    cases, userRole = None, None 
    if Case.objects.filter(reporter_name=fullname).exists(): 
        cases = Case.objects.filter(reporter_name=fullname)
        userRole = "reporter" 
    elif Case.objects.filter(investigator=fullname).exists():
        cases = Case.objects.filter(investigator=fullname)
        userRole = "investigator"
    else: 
        pass
    params = {'username':username, 'fullname':fullname, 'cases':cases, 'userRole':userRole}
    return render(request, 'main/adminPanel.html', params)


def updateData(request, id):
    if request.method== 'POST':
        record = Case.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=record) # Generating a form with the values of the record with the given id
        if fm.is_valid():
            fm.save()
    else:
        record = Student.objects.get(pk=id)
        fm = StudentRegistration(instance=record) 
    return render(request, 'main/update_data.html', {'form':fm})
    # return HttpResponse("update data")


def deleteData(request, id):
    if request.method == 'POST':
        record = Case.objects.get(pk=id) 
        reporter_name = record.reporter_name
        username = request.user.username
        record.delete()
        return redirect('/main/dashboard/'+username)
