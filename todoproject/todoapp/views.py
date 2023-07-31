from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse,JsonResponse
from .forms import RegistrationForm
from .models import UserProfile
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import authenticate, login


# Create your views here.
def index(request):
    return render(request,'index.html')

def submit(request):
    obj = Todo()
    obj.title = request.GET['title']
    obj.description = request.GET['description']
    obj.priority = request.GET['priority']
    obj.save()
    mydictionary = {
        "alltodos" : Todo.objects.all()
    }
    return render(request,'list.html',context=mydictionary)

def delete(request,id):
    obj = Todo.objects.get(id=id)
    obj.delete()
    mydictionary = {
        "alltodos" : Todo.objects.all()
    }
    return render(request,'list.html',context=mydictionary)

def list(request):
    mydictionary = {
        "alltodos" : Todo.objects.all()
    }
    return render(request,'list.html',context=mydictionary)
#  сортировка
def sortdata(request):
    mydictionary ={
        "alltodos" : Todo.objects.all().order_by('priority')
    }
    return render(request,'sort.html',context=mydictionary)

def searchdata(request):
    q = request.GET['query']
    mydictionary = {
        "alltodos" : Todo.objects.filter(title__contains=q)
    }
    return render(request,'list.html',context=mydictionary)

def edit(request,id):
    obj = Todo.objects.get(id=id)
    mydictionary = {
        "title" : obj.title,
        "description" : obj.description,
        "priority" : obj.priority,
        "id" : obj.id
    }
    return render(request,'edit.html',context=mydictionary)


def update(request,id):
    obj = Todo(id=id)
    obj.title = request.GET['title']
    obj.description = request.GET['description']
    obj.priority = request.GET['priority']
    import datetime
    updated_at = datetime.datetime.now()
    obj.created_at = updated_at
    obj.save()
    mydictionary = {
        "alltodos" : Todo.objects.all()
    }
    return render(request,'list.html',context=mydictionary)

# datee
def my_view(request):
    my_date = "2023-07-29" 
    return render(request, 'list.html', {'my_date': my_date})

    # register



def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login') 
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')  
            else:
                pass
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})