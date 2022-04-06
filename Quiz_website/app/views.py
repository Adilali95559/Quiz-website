from django.shortcuts import render,HttpResponse,redirect
from datetime import datetime
from app.models import Contact
from django.contrib import messages
from . import forms
from .import models
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent !')
        
    return render(request, "contact.html")

def quiz(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
         login(request,user)
    # A backend authenticated the credentials
         messages.success(request, 'Your are login !')
         return redirect('/')
        else:
    # No backend authenticated the credentials

         return render(request, "quiz.html")
        
    return render(request, "quiz.html")     

def home(request):
    catData=models.QuizCategory.objects.all()
    return render(request, "home.html",{'data': catData})

def register(request):
    form=forms.RegisterUser
    if request.method=='POST':
        form=forms.RegisterUser(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your are register!')

    return render(request, "registert.html",{'form':form})

def category_question(request,cat_id):
    if request.user.is_anonymous:
        
        return redirect('/quiz')
        

    category=models.QuizCategory.objects.get(id=cat_id)
    question=models.QuizQuestion.objects.filter(category=category).order_by('id').first()
    return render(request, "category-questions.html",{'question':question,'category':category})


def submit_answer(request,cat_id,quest_id):
  if request.method=='POST':
    category=models.QuizCategory.objects.get(id=cat_id)
    question=models.QuizQuestion.objects.filter(category=category,id__gt=quest_id).exclude(id=quest_id).order_by('id').first()
    quest=models.QuizQuestion.objects.get(id=quest_id)
    user=request.user
    answer=request.POST['answer']
    models.UserSubmittedAnswer.objects.create(user=user,question=quest,right_answer=answer)
   

    if question:
     return render(request, "category-questions.html",{'question':question,'category':category})
    else:
     result=models.UserSubmittedAnswer.objects.filter(user=request.user)
     
     rigthAns=0
     for row in result:
         if row.question.right_opt == row.right_answer:
             rigthAns+=1
     return render(request, "result.html",{'result':result,'rigthAns':rigthAns},)
  else:
    return HttpResponse('Method not allowed !')


def logoutUser(request):
    logout(request)
    return redirect('/quiz')



