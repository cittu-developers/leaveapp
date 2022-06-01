from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import *


from .models import User, Country,Gender
from .forms import MyUserCreationForm,UserForm
from registry.models import *

# Create your views here.
@login_required(login_url='login')
def index(request):
    return render(request, 'home/index.html')


def loginPage(request):
    msg=None
    userlogin = request.user
    # print(userlogin.id)
    if request.method == "POST":
        username_var = request.POST.get('username')
        password_var = request.POST.get('password')
        user = authenticate(request,username=username_var, password=password_var)

        qs = User.objects.filter(username=username_var)
        if len(qs) < 1:
            msg = 'This user does not EXIST!'
        
        try:
            user = User.objects.get(username=username_var)
        except:
            user = None
        if user is not None and not user.check_password(password_var):
            msg = 'Wrong Password'
        elif user is None:
            pass
        else:     
            login(request, user)
            # messages.success(request, "Welcome" + " " + str(userlogin))
            if "next" in request.POST:
                return redirect(request.POST.get('next'))
            else:
                if Head.objects.filter(user_id=request.user.id).exists():
                    return HttpResponseRedirect("Leave_list_by_departments")
                else:
                    return redirect("index")

    context = {"msg":msg}
    return render(request, 'accounts/login.html', context)

#logoutUser views
def logoutUser(request):
    logout(request)
    return redirect('login')

#registerUser views
@login_required(login_url='login')
def registerUser(request):
    gend = Gender.objects.all()
    cont = Country.objects.all()
    unit = Unit.objects.all()
    dept = Department.objects.all()
    direct = Directorate.objects.all()
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        other_name = request.POST['other_name']
        file_number = request.POST['file_number']
        username = request.POST['username']
        date_of_birth = request.POST['date_of_birth']
        gender = request.POST['gender']
        nationality = request.POST['nationality']
        directorate = request.POST['directorate']
        department = request.POST['department']
        unit       = request.POST['unit']
        # sub_unit   = request.POST['sub_unit']
        passport = request.FILES['passport']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
    
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Exists')
                return redirect('register')

            elif User.objects.filter(file_number=file_number).exists():
                messages.info(request, 'File Number Already Exists  ') 
                return redirect('register')  
            else:
                user = User.objects.create_user(first_name=first_name,last_name=last_name,other_name=other_name,file_number=file_number,
                                                username=username,date_of_birth=date_of_birth,
                                                gender_id=gender,nationality_id=nationality,
                                                directorate_id=directorate,department_id=department,
                                                unit_id=unit,passport=passport,password=password1)
                user.save();
                messages.info(request, "Register successful")

                return redirect('employment_detail',id=user.id)
        else:
            messages.info(request, "Password Not Matching")
            return redirect('register')
    context = {'gend':gend,'cont':cont,'unit':unit,'dept':dept,'direct':direct}                 
    return render(request, 'accounts/register.html', context)


#userProfile views
@login_required(login_url='login')
def userProfile(request):
    args = {'user':request.user,}
    
    return render(request, 'home/index.html',args )
@login_required(login_url='login')
def staff_biodata_summary(request,id):
    user = User.objects.get(id=id)
    context= {'user':user}
    return render(request, 'accounts/staff_biodata_summary.html', context )


#updateUser views
@login_required(login_url='login')
def updateUser(request):
    user = request.user
    form = UserForm(instance=user)

    if request.method == 'POST':
        form = UserForm(request.POST,request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('index')#, pk=user.id

    return render(request, 'accounts/updateprofile.html', {'form': form})

