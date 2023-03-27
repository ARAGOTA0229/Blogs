from django.shortcuts import render,redirect
from .models import *
from django.views.generic import DetailView
from django.contrib import messages
# Create your views here.

def Index(request):
    context={
        'main1':Main.objects.all(),
        'result':Welcome.objects.first(),
        'slider':Slider.objects.all(),
        'photo1':BigPhoto.objects.first(),
        'bigslider':BigSlide.objects.all(),
        'stat':Stat.objects.all(),
        'team':Team.objects.all(),
        'commenting':Comments.objects.all(),
        'blog':Bloging.objects.all()
    }
    return render(request,'index.html',context)

def About(request):
    about=AboutSlide.objects.first()
    context={
        'about':about,
        'team':Team.objects.all()
    }
    return render(request,'about.html',context)

def Comment(request):
    entername:Experience.objects.all()
    context={
        'comment':Comments.objects.all(),
    
    }
    return render(request,'comment.html',context,entername)

def Send_msg(request):
    if request.method == 'POST':
        r = request.POST    
        category = r['category']
        name = r['name']
        text = r['text']
        # orign = r['orign']

        Comments.objects.create(category=category,name=name,text=text)



    return redirect('/comment/')
# def Blog(request):
#     return render(request,'blog-single.html')

class BlogDetail(DetailView):
    
    model=Bloging
    template_name='blog-single.html'
    context_object_name ='bloger'

def Post_Com(request,):
    if request.method =='POST':
        r= request.POST 
        name = r['name']
        email = r['email']
        text = r ['text']
        Izoh.objects.create(name=name,email=email,text=text)
        
        return redirect('http://127.0.0.1:8000/blogdetail/id/')
    
def Contact(request):
    contact =Contacpage.objects.first()
    context={
        'conpage':contact,
        'con':Experience.objects.first()
    }
    return render(request,'contact.html',context)
   
def Send_msg(request):
    if request.method =='POST':
        r= request.POST 
        name = r['name']
        email = r['email']
        phone=r['phone']
        text = r ['text']
        Message.objects.create(name=name,email=email,phone=phone,text=text)
        info='<strong>{}</strong>. Your message has succesfully send!!,As soon as they will answer your response'.format(r)
        messages.success(request,info)
        
        return redirect('/contact/')        

def Practise(request):
    return render(request,'practice-areas.html')

def New(request):
    context={
        'news':News.objects.all()
    }
    return render(request,'news.html',context)
