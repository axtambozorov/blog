from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from .models import New,Category
from .forms import UserForm,UserLoginForm
from django.contrib.auth import login, logout
# Create your views here.

def home(request):
    content = New.objects.all()
    context = {
        'news':content,
        'categories':Category.objects.all()
    }
    return render(request,'base.html',context)


def get_category(request,category_id):
   news=Category.objects.all(),

   context ={
       'categories':New.objects.filter(category_id=category_id),
       'news':news,
   }
   return render(request,'news/category.html',context)

def register(request):

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserForm()
    return render(request,'news/register.html',{ 'form':form })

def user_login(request):
    if request.method == 'POST':
        form= AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('home')
    else:
        form=UserLoginForm()
    return render(request,'news/login.html',{'form':form})

def user_logout(request):
    logout(request)
    return redirect('home')

def detail(request,new_id):
    new=New.objects.get(id=new_id)
    return render(request,'news/detail.html', {'new':new})