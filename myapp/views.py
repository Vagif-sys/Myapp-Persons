from django.shortcuts import render,redirect
from django.db.models import Q
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Person,Comment
from.forms import PersonForm,CreateUserForm,CommentForm
from.filters import PersonFilter
from .decorators  import unauthenticated_user,allowed_users,admin_only
# Create register program and unauthenticated user page
@unauthenticated_user
def register(request):
    form = CreateUserForm()
    if request.method =="POST": 
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='persons')
            user.groups.add(group)
            messages.success(request,'Account was created for ' + username)
            return redirect('login')  


    context = {'form':form}
    return render(request,'myapp/register.html',context)

# Create login page
@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('base')
        else:
            messages.info(request,'User or Password is incorrect')
    context = {}
    return render(request,'myapp/login.html',context)
# Create logout 
def logOutUser(request):
    logout(request)
    return redirect('login')



@login_required(login_url='login')
@admin_only
def base(request):
    person = Person.objects.all()
    context = {'person':person}
    return render(request,"myapp/dashboard.html",context)

@login_required(login_url='login')
def create_person(request):
    form = PersonForm()
    if request.method =='POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save() 
        return redirect('seach')
    else:
         form = PersonForm()
    return render(request,"myapp/create_person.html",{'form':form})

def home(request):
    return render(request,"myapp/home.html")


def user(request):
    if request.method == 'POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            form.save()
    else:
          form = CommentForm()
    comm = Comment.objects.all()
    context = {'comm':comm,'form':form}
    comm = Comment.objects.all()
    return render(request,"myapp/user.html",context)

@login_required(login_url='login')
def dashboard(request):
    person =Person.objects.all()
    context = {'person':person}
    return render(request,'myapp/dashboard.html',context)

@login_required(login_url='login')
def update_person(request,id):
    if request.method =='POST':
       person = Person.objects.get(pk=id)
       form = PersonForm(request.POST,instance=person)
       if form.is_valid():
           form.save()
       return redirect('dashboard')
    else:
        person = Person.objects.get(pk=id)
        form = PersonForm(instance=person)
    return render(request,"myapp/update_person.html",{'form':form})

def delete_person(request,id):
    person = Person.objects.get(pk=id)
    if request.method =='POST':
       person.delete()
       return redirect('seach')
    context={'person':person}
    return render(request,"myapp/delete_person.html",context) 

def __str__(self):
    return self.name

def seach2(request):
    query = request.GET.get('q')
    person = Person.objects.filter(Q(name__icontains=query) | Q(gender__icontains=query)).distinct()
    return render(request,'myapp/seach2.html',{'person':person})
