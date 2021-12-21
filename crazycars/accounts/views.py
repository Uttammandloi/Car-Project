from django.shortcuts import render ,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.shortcuts import render
from contact.models import contact
from django.contrib.auth.decorators import login_required

def Login(request):
    
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,'You logged in sucessfully')
            return redirect('dashboard')
        else:
            messages.error(request,'Invalid login credential')
            return redirect('login')
            
    return render(request,"accounts/login.html")

def Register(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password == confirm_password:
            
            if User.objects.filter(username=username).exists():
                messages.error(request,'user is already exists!')
                return redirect('register')
                
            else:
                
                if User.objects.filter(email=email).exists():
                     messages.error(request,'email is already exists!')
                     return redirect('register')
                
                else:
                    user = User.objects.create_user(first_name=firstname,last_name=lastname,username=username,email=email,password=password)
                    #auth.login(request, user)
                    #messages.success(request,'You are login successfully!')
                    #return redirect('dashboard')
                    user.save()
                    messages.success(request,'You are register successfully!')
                    return redirect('login')
                    
        
        else:
            messages.error(request,'password do not match!')
            return redirect('register')
            

    else:
        return render(request,"accounts/register.html")

@login_required(login_url='login')
def Dashboard(request):
    user_inquery = contact.objects.order_by('created_date').filter(user_id=request.user.id)
    data={
        
        "inquaries":user_inquery
    }
    return render(request,"accounts/dashboard.html",data)

def Logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    return redirect("home")
 