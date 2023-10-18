from django.shortcuts import render,redirect
from django.http import HttpResponse

from .forms import *
from .models import *
import os
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from django.contrib.auth import logout
# user model is a bydefualt django model which is used for authentication.
# fields of user models are username firstname lastname email password


def bnkfun(request):
    if request.method == 'POST':
        a=bnkf(request.POST,request.FILES)
        if a.is_valid():
            fn=a.cleaned_data['fname']
            ln=a.cleaned_data['lname']
            un=a.cleaned_data['uname']
            em=a.cleaned_data['email']
            ph=a.cleaned_data['phn']
            ac=int("15"+str(ph))
            im=a.cleaned_data['img']
            ps=a.cleaned_data['psw']
            cps=a.cleaned_data['cpsw']
            if ps == cps:
                b = bnkm(fname=fn, lname=ln, uname=un, email=em, phn=ph,acc_number=ac, img=im, psw=ps,balance=0)
                b.save()
                subject= "your account has been created"
                #f is used to get variable ac,othervise it remain as a strng
                message= f"your new account number is {ac}"
                email_from= "lachusibi414@gmail.com"
                email_to=em
                send_mail(subject,message,email_from,[email_to])
                return redirect(banknew)
                # return HttpResponse("Registartion success")
            else:
                return HttpResponse('Password doesnt match')
        else:
            return HttpResponse("failed")
    return render(request,'bnk2.html')


def banknew(request):
    if request.method == "POST":
        a = bankform(request.POST)
        if a.is_valid():
            fn = a.cleaned_data['fname']
            ps = a.cleaned_data['psw']
            b = bnkm.objects.all()
            for i in b:
                if i.fname == fn and i.psw == ps:
                    request.session['id']=i.id          #this is used for accesing id globaly
                    return redirect(profile)
                    return HttpResponse('login success')
            else:
                return HttpResponse('login failed')

        return HttpResponse("failed")
    return render(request, 'bnk.html')


def index(request):
    return render(request,'index.html')

def profile(request):
    #for handling error or exception
    try:
        id1 = request.session['id']
        a = bnkm.objects.get(id=id1)
        img = str(a.img).split('/')[-1]
        return render(request, 'filebnk.html', {'a': a, 'img': img})
    except:
        return redirect(banknew)


def edit1(request,id):
    a=bnkm.objects.get(id=id)
    if request.method== 'POST':
        a.fname=request.POST.get('fname')
        a.lname=request.POST.get("lname")
        a.email=request.POST.get('email')
        a.phn=request.POST.get('phn')
        a.uname=request.POST.get('uname')
        a.save()
        return redirect(profile)
    return render(request,'edit.html',{'a':a})


def fileedit(request,id):
    a=bnkm.objects.get(id=id)
    img=str(a.img).split('/')[-1]
    if request.method =='POST':
        a.uname=request.POST.get('uname')
        # fr imge
        if len(request.FILES) !=0:
            if len(a.img)>0:
                os.remove(a.img.path)
            a.img=request.FILES['img']
        a.save()
        return redirect(profile)
    return render(request,'imgedit.html',{'a':a,'img':img})


# def imaged(request, id):
#     a = bnkm.objects.get(id=id)
#     img = str(a.img).split('/')[-1]
#     if request.method == 'POST':
#
#         if request.FILES.get('img') == None:
#             a.save()
#         else:
#             a.img =request.FILES['img']
#         a.save()
#         return redirect(profile)
#     return render(request, 'imgedit.html', {'a': a, 'img': img})



def amountadd(request,id):
    x=bnkm.objects.get(id=id)
    if request.method=='POST':
        am=request.POST.get('amount2')
        request.session['am']=am
        ac = x.acc_number
        request.session['ac'] = ac
        x.balance+=int(am)
        x.save()
        b=addamount(amount2=am,uid=request.session['id'])
        b.save()
        pin=request.POST.get('psw1')
        if pin==x.psw:
            return redirect(tickmrk)
        else:
            return HttpResponse('amount added failed')

    return render(request,'add_amount.html')

def tickmrk(request):
    am=request.session['am']
    ac=request.session['ac']
    return render(request,'tick.html',{'am':am,'ac':ac})


def wdrawamount(request,id):
    x=bnkm.objects.get(id=id)
    if request.method =='POST':
        wd=request.POST.get('amount1')
        request.session['wd']=wd
        ac=x.acc_number
        request.session['ac']=ac
        x.balance-=int(wd)
        x.save()
        b=widamount(amount1=wd,uid=request.session['id'])
        b.save()
        pin=request.POST.get('psw1')
        if pin==x.psw:
            return redirect(tickmar)
        else:
            return HttpResponse('No Amount')

    return render(request,'wthdrw.html')

def tickmar(request):
    wd=request.session['wd']
    ac=request.session['ac']
    return render(request,'tickmark.html',{'wd':wd,'ac':ac})


def check(request,id):
    x=bnkm.objects.get(id=id)
    if request.method=='POST':
        ac = x.acc_number
        request.session['ac'] = ac
        bal=x.balance
        request.session['bal']=bal
        x.save()
        pin=request.POST.get('psw1')
        if pin==x.psw:
            return redirect(success)
        else:
            return HttpResponse('Error')
    return render(request,'balance.html')

def success(request):
    bal=request.session['bal']
    ac=request.session['ac']
    return render(request,'balancesuccess.html',{'ac':ac,'bal':bal})

def depo(request):
    x=addamount.objects.all()
    id=request.session['id']
    return render(request,'deposit.html',{'x':x,'id':id})

def wdraw(request):
    x=widamount.objects.all()
    id=request.session['id']
    return render(request,'wdrwtable.html',{'x':x,'id':id})


def ministate(request,id):
    a=bnkm.objects.get(id=id)
    pin=request.POST.get('psw1')
    if request.method=='POST':
        if pin==a.psw:
            choice=request.POST.get('select')
            if choice=='deposit':
                return redirect(depo)
            elif choice== 'withdraw':
                return redirect(wdraw)
        else:
            return HttpResponse("Password error")
    return render(request,'statement.html')


def newss(request):
    if request.method=='POST':
        a=newsf(request.POST,request.FILES)
        if a.is_valid():
            ti=a.cleaned_data['title']
            con=a.cleaned_data['content']
            b=newsm(title=ti,content=con)
            b.save()
            return redirect(admnds)
            # return HttpResponse(" news feed added successfully")
        else:
            return HttpResponse("failed")
    return render(request,'news.html')


def dis(request):
    a=newsm.objects.all()
    return render(request,'display.html',{'a':a})

def admnds(request):
    a=newsm.objects.all()
    return render(request,"displ2.html",{'a':a})


def editadmn(request,id):
    a=newsm.objects.get(id=id)
    if request.method=='POST':
        a.title=request.POST.get('title')
        a.content=request.POST.get('content')
        a.save()
        return redirect(admnds)
    return render(request,'eedit.html',{'a':a})


def deladmn(request,id):
    a=newsm.objects.get(id=id)
    a.delete()
    return redirect(admnds)


# def tablsrch(request):
#     a=newsm.objects.all()
#     return render(request,'tblsrch.html',{"a":a})


def wish(request,id):
    a=newsm.objects.get(id=id)
    wish=wishlist.objects.all()
    for i in wish:
        if i.newsid == a.id and i.uid == request.session['id'] :
            return HttpResponse("item already in wishlist")
    b=wishlist(title=a.title,content=a.content,date=a.date,newsid=a.id,uid=request.session['id'])
    b.save()
    return HttpResponse("added to wishlist")


def wishl(request):
    a=wishlist.objects.all()
    id=request.session['id']
    return render(request,'wsh list.html',{'a':a,'id':id})

# def adminlog(request):
#     if request.method=='POST':
#         a=adminf(request.POST)
#         if a.is_valid():
#             em=a.cleaned_data['email']
#             us=a.cleaned_data['username']
#             b=User.objects.all()
#             for i in b:
#                 if em==i.email and us==i.username:
#                     return redirect(adminpro)
#                     return HttpResponse("admin logged")
#             else:
#                 return HttpResponse("login failed")
#
#     return render(request,'adminlogin.html')
##### \\use authentication method for accessing password\\
##  authentication function that checks credentials against the authentication  backend and return it.
def adminlog(request):
    if request.method=='POST':
        a=adminf(request.POST)
        if a.is_valid():
            us=a.cleaned_data['username']
            ps=a.cleaned_data['password']
            user=authenticate(request,username=us,password=ps)
            if user is not None:
                    return redirect(adminpro)
                    return HttpResponse("admin logged")
            else:
                return HttpResponse("login failed")

    return render(request,'adminlogin.html')

def adminpro(request):
    return render(request,'adminprofile.html')


def logout_view(request):
    logout(request)
    return redirect(index)

def forgot_password(request):
    a=bnkm.objects.all()
    if request.method == 'POST':
        em= request.POST.get('email')
        ac= request.POST.get('acc_number')
        for i in a:
            if(i.email==em and i.acc_number==int(ac)):
                id=i.id
                subject="Password Change"
                message=f"http://127.0.0.1:8000/bank_app/change/{id}"
                # message="Renew your password"
                frm="lachusibi414@gmail.com"
                to=em
                send_mail(subject,message,frm,[to])
                return HttpResponse("Check Your E-mail")
        else:
            return HttpResponse("Sorry, Some Error Occured")
    return render(request,'forgot.html')


def change_password(request,id):
    a=bnkm.objects.get(id=id)
    if request.method=='POST':
        p1=request.POST.get('psw1')
        p2=request.POST.get('cpsw')
        if p1==p2:
            a.psw=p1
            a.save()
            return HttpResponse('Password changed')
        else:
            return HttpResponse('Sorry!!')
    return render(request,'change.html')

