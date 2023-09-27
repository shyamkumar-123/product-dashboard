from django.shortcuts import render,redirect
#from django.http import HttpResponse
from blogapp.models import Product
from django.db.models import Q
from blogapp.forms import EmpForm,ProductForm,UserRegister
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login

def Home(request):
    return render(request,'home.html')

def about(request):
    print("Hello from views function")
    return render(request,'about.html')

def staticfile(request):
    return render(request,'learnstatic.html')

def addproduct(request):
    #print("Method=",request.method)
    user_id=request.user.id
    #print("Logged in user id:",user_id)
    if request.method=="POST":
        #print("Post request in post section")
        product_name=request.POST['pname']
        cat=request.POST['cat']
        amount=request.POST['amt']
        status=request.POST['status']

        p=Product.objects.create(name=product_name,cat=cat,price=amount,status=status,uid=user_id)     
        p.save()
        #return HttpResponse("Record inserted successfully")
        return redirect('dashboard')

    else:
        #print("Get request else section")
        return render(request,'addproduct.html')
    
def dashboard(request):
    #qset=Product.objects.all()
    user_id=request.user.id
    qset=Product.objects.filter(uid=user_id)
    #print(qset)
    content={}
    content['data']=qset
    return render(request,'dashboard.html',content)
           # [OR]
'''def dashboard(request):
    qset=Product.objects.all()
    return render(request,'dashboard.html',{'qset':qset})'''



def delete(request,rid):
    qset=Product.objects.get(id=rid)
    qset.delete()
    return redirect('dashboard')

def edit(request,rid):
    if request.method=="POST":
    
        product_name=request.POST['pname']
        cat=request.POST['cat']
        amount=request.POST['amt']
        status=request.POST['status']

        p=Product.objects.filter(id=rid)
        p.update(name=product_name,cat=cat,price=amount,status=status)
        return redirect('dashboard')
    else:
        P=Product.objects.filter(id=rid)
        content={}
        content['data']=P
        return render(request,'edit.html',content)
    
    #filters start
def catfilter(request,cv):
    #if cv=="1":
    p=Product.objects.filter(cat=cv)
    #print(p)
    content={}
    content['data']=p
    return render(request,'dashboard.html',content)

             #(or)

'''def catfilter(request,cv):
    if cv=='1':
        p=Product.objects.filter(cat=1')
    elif cv=='2':
        p=Product.objects.filter(cat=2)
    else:
        p=Product.objects.filter(cat=3)
    content={}
    content['data']=p
    return render(request,'dashboard.html',content)'''

def statusfilter(request,sv):
    p=Product.objects.filter(status=sv)
    content={}
    content['data']=p
    return render(request,'dashboard.html',content)

            #[or]

'''def statusfilter(request,sv):
    if sv=="1":
        p=Product.objects.filter(status=1)
    else:
        p=Product.objects.filter(status=0)
    content={  }
    content['data']=p
    return render(request,'dashboard.html',content)'''
  

def sortfilter(request,x):
    if x=='0':
        p=Product.objects.order_by('price')
    else:
        p=Product.objects.order_by('-price')
    
    content={}
    content['data']=p
    return render(request,'dashboard.html',content)



def pricefilter(request,x):
    if x=="1":
        #p=Product.objects.filter(price__gte=13000)
        # use orderby and filter by at once
        p=Product.objects.order_by('price').filter(price__gte=13000)


    else:
        p=Product.objects.filter(price__lt=13000)


    content={}
    content['data']=p
    return render(request,'dashboard.html',content)


def multifilter(request):
    if request.method=="POST":
        cv=request.POST['category']
        sv=request.POST['status']
       # price=request.POST['amt']

        q1=Q(cat=cv)
        q2=Q(status=sv)
        #q3=Q((price__gte=13000) and price__lt=13000))
        p=Product.objects.filter(q1 & q2 )
        content={}
        content['data']=p
        return render(request,'dashboard.html',content)
    
#Django forms.
def django_form(request):
    if request.method=="POST":
        name=request.POST['empname']
        mob=request.POST['mobile']
        dept=request.POST['department']
        dt=request.POST['date_of_joining']
        print("Employee:",name)
        print("Mobile:",mob)
        print("Department:",dept)
        print("Date of joining:",dt)
    else:
        dfobj=EmpForm()
        #print(dfobj)
        content={}
        content['form']=dfobj
        return render(request,'empform.html',content)

#Model forms.
def modelform(request):
    if request.method=='POST':
        pass
    else:
        mfobj=ProductForm()
        #print(mfobj)
        content={'form':mfobj}
        return render(request,'addproductmodel.html',content)

 #User registration form.     
def user_register(request):
    if request.method=="POST":
       regfm=UserRegister(request.POST)
       #print(regfm.is_valid())
       # print(regfm)
       if regfm.is_valid():
            content={}
            regfm.save()
            content['msg']="User Registered Successfully"
            return render(request,'success.html',content)
    else:
        regfm=UserRegister()
        #print(regfm)
        content={}
        content['regfm']=regfm
        return render(request,'register.html',content)
 
def user_login(request):
    if request.method=="POST":
        logfm=AuthenticationForm(request=request,data=request.POST)
        #print(logfm)
        if logfm.is_valid():
            uname=logfm.cleaned_data['username']
            upass=logfm.cleaned_data['password']
            #print(uname)
            #print(upass)
            res=authenticate(username=uname,password=upass)
            #print(res)
            if res:
                login(request,res)
                return redirect("dashboard")

    else:
        logfm=AuthenticationForm()
        #print(logfm)
        content={}
        content['form']=logfm
        return render(request,'login.html',content)

def setcookie(request):
    res=render(request,'setcookie.html')
    res.set_cookie('name','Itvedant')
    res.set_cookie('rno',37)

    return res


def getcookie(request):
    name=request.COOKIES['name']
    rnum=request.COOKIES['rno']
    content={}
    content['n']=name
    content['r']=rnum
    return render(request,'getcookie.html',content)

def setsession(request):
    request.session['name']="Itvedant Eclass"
    return render(request,'setsession.html')


def getsession(request):
    content={}
    content['n']=request.session['name']
    return render(request,'getsession.html',content)