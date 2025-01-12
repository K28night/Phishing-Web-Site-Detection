from urllib import request
from django.shortcuts import render,redirect
from .models import*
from .forms import*
import requests
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth  import logout

# Create your views here.

def index(request):
    return render(request,'index.html')

def feedback(request):
    if request.method=='POST':
        id=request.POST.get('id')
        fname=request.POST.get('fname')
        bk=request.POST.get('bk')
        feedbackmodel(fname=fname,bk=bk).save()
    return render(request,'feedback.html')
    
def about1(request):
    return render(request,'about1.html')

def predict(request):
    return render(request,'predict.html')

def is_client(user):
    return user.groups.filter(name='client').exists()

def afterlogin_view(request):
    if is_client(request.user):
        return redirect('home')

@login_required(login_url='login')
@user_passes_test(is_client)
def contact(request):
    result=""
    
    if request.method=="POST":
        submitbutton=request.POST.get(all)
    area=""
    
    form= predictForm(request.POST or None)
    if form.is_valid():
        area= form.cleaned_data.get("area")
        # result=summarize(area)
        # print("",result)
        website=""
        website="https://ipqualityscore.com/api/json/url/1ccoiAdXjhPLKzq83pmev7bb9mLK6rxt/" +area
        result=requests.get(website)
        
        data=result.json()
        # category=""
        # domain=""

        a1=data['category']
        a2=data['domain']
        a3=data['ip_address']
        a4=data['server']
        a5=data['malware']
        a6=data['spamming']
        a7=data['phishing']
        a8=data['risk_score']
        a9=data['suspicious']
        a10=data['domain_rank']



       
        print("",data)

        spammodel(category=a1,domain=a2,ip_address=a3,server=a4,malware=a5,spamming=a6,phishing=a7,risk_score=a8,suspicious=a9,domain_rank=a10).save()
        


        
        context={
            "entered_text":a1,
            "entered_domain":a2,
            "entered_a1":a3,
            "entered_a2":a4,
            "entered_a3":a5,
            "entered_a4":a6,
            "entered_a5":a7,
            "entered_a6":a8,
            "entered_a7":a9,
            "entered_a8":a10,
            

          

            
            
        }
        return render(request,'predict.html',context=context)
    else:
        return render(request,'contact.html')
   



def register(request):
    form=registerform()
    form1=registrationform()
    mydict={'form':form,'form1':form1}
    if request.method=='POST':
        form=registerform(request.POST)
        form1=registrationform(request.POST)
        if form.is_valid() and form1.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()
            registrationmodel=form1.save(commit=True)
            registrationmodel.user=user
            registrationmodel.save()
            messages.success(request,'Registration success')
            group=Group.objects.get_or_create(name='client')
            group[0].user_set.add(user)
            return redirect('login') 
    return render(request,'register.html',context=mydict)

def is_client(user):
    return user.groups.filter(name='client').exists()

def adminregister(request):
    form=registerform1()
    # 
    mydict={'form':form}
    if request.method=='POST':
            form=registerform1(request.POST)
            
            if form.is_valid():
                user=form.save()
                user.set_password(user.password)
                user.save()
          
                messages.success(request,'Registration success')
                group=Group.objects.get_or_create(name='admin')
                group[0].user_set.add(user)
                return redirect('login')
    return render(request,'adminregister.html',context=mydict)

def is_admin(user):
    return user.groups.filter(name='admin').exists()

def afterlogin_view(request):
    if is_client(request.user):
        return redirect('home')
    elif is_admin(request.user):
        return redirect('admindash')


def login(request):
    return render(request,'login.html')
    
def test(request):
    return render(request,'test.html')

@login_required(login_url='login')
@user_passes_test(is_client)
def home(request):
    result=""
    
    if request.method=="POST":
        submitbutton=request.POST.get(all)
    area=""
    
    form= predictForm(request.POST or None)
    if form.is_valid():
        area= form.cleaned_data.get("area")
        # result=summarize(area)
        # print("",result)
        website=""
        website="https://ipqualityscore.com/api/json/url/1ccoiAdXjhPLKzq83pmev7bb9mLK6rxt/" +area
        result=requests.get(website)
        
        data=result.json()
        # category=""
        # domain=""

        a1=data['category']
        a2=data['domain']
        a3=data['ip_address']
        a4=data['server']
        a5=data['malware']
        a6=data['spamming']
        a7=data['phishing']
        a8=data['risk_score']
        a9=data['suspicious']
        a10=data['domain_rank']

       
        print("",data)
      

        


        
        context={
            "entered_text":a1,
            "entered_domain":a2,
            "entered_a1":a3,
            "entered_a2":a4,
            "entered_a3":a5,
            "entered_a4":a6,
            "entered_a5":a7,
            "entered_a6":a8,
            "entered_a7":a9,
            "entered_a8":a10,
            

          

            
            
        }
        return render(request,'predict.html',context=context)
    else:
        return render(request,'home.html')


    return render(request,'home.html')

def logout_request(request):
    logout (request)
    return redirect('index')


def profile_edit(request):
    far=registrationmodel.objects.get(user_id=request.user.id)
    if request.method=='POST':
        far=registrationmodel.objects.get(user_id=request.user)
        form=registerform(request.POST,instance=far.user)
        form4=registrationform(request.POST,instance=far)
        if form.is_valid() and form4.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()
            form4.save()
            messages.success(request,'Profile edit success')
            return redirect('home')

    else:
        form=registerform(instance=far.user)
        form4=registrationform(instance=far)
        context={'form':form,'form4':form4,}


    return render(request,'profile_edit.html', context)



def report(request):
    form=reportform()
    mydict={'form':form}
    if request.method=='POST':
        form=reportform(request.POST)
        if form.is_valid() :
            user1=form.save()
            user1.save()
            return redirect('home')
            
    return render(request,'report.html',context=mydict)

def userdetailsview(request):
    cr=registrationmodel.objects.all()
    return render(request,'userdetailsview.html',{'cr':cr})

def delete1(request,pk):
  cr=registrationmodel.objects.get(id=pk)

  cr.delete()
  return redirect('/userdetailsview') 



def delete2(request,pk):
  cr=reportmodel.objects.get(id=pk)

  cr.delete()
  return redirect('/reportsview') 

  
def delete3(request,pk):
  cr=feedmodel.objects.get(id=pk)

  cr.delete()
  return redirect('/feedbackview') 

def delete4(request,pk):
  cr=spammodel.objects.get(id=pk)

  cr.delete()
  return redirect('/sitesinformation') 


def reportsview(request):
    cr=reportmodel.objects.all()

    return render(request,'reportsview.html',{'cr':cr})


def feedbackview(request):
    cr=feedmodel.objects.all()

    return render(request,'feedbackview.html',{'cr':cr})

def admindash(request):
    return render(request,'admindash.html')

def sitesinformation(request):
    cr=spammodel.objects.all()

    return render(request,'sitesinformation.html',{'cr':cr})

def usersiteview(request):
    cr=spammodel.objects.all()

    return render(request,'usersiteview.html',{'cr':cr})


def feedback(request):
    far=registrationmodel.objects.get(user_id=request.user.id)
    cr=far.user.email
    print(cr)
    feed1=FeedForm(instance=far.user)
    mydict={'far':far,'feed1':feed1}         

    if request.method=="POST":

        feed1=FeedForm(request.POST)
        if feed1.is_valid():
            user2=feed1.save()
            user2.user=request.user
            user2.save()
            messages.success(request,'Registration success')
            return redirect('home')
    else:
        # feed1=FeedForm(instance=far.user)
   
        print("invalid form")    
    return render(request,'feedback.html',context=mydict)