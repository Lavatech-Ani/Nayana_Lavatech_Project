from django.shortcuts import render
from .forms import Enquiry, AddmissionForm, BatchForm, ModifyForm
from .models import Enq, Addmission, Batch, Modify
from django.http import HttpResponse, JsonResponse
from django.utils.dateformat import DateFormat
from django.utils.formats import get_format
from datetime import datetime
from django.db.models import F
import json


# Create your views here

def index(request):
    return render(request,'index.html')

def enq(request):
    posts = Enq.objects.latest('enqid')
    posts = posts.enqid
    thank = False
    if request.method == 'POST':
      form = Enquiry(request.POST)
      if form.is_valid():
        form.save()
        thank = True 
      else:
          print('wrong')
          print(form.errors)
    newid = posts + 1
    form = Enquiry(initial={'enqid': newid})
    context = {'form':form,'thank': thank}
    return render(request,'enq.html',context)  

def StudentAlias(request):
    print("select student alias")
    posts = Enq.objects.all()
    if request.method == 'POST': 
        add_alias = request.POST.get('browsers','')
        ans = Enq.objects.filter(enqalias=add_alias)
        for x in ans:
            form = AddmissionForm(initial={'add_alias':x.enqalias,'add_id':x.enqid,'fname':x.fname,'lname':x.lname,'email':x.email,
            'phone':x.phone,'Address':x.Address})
    return render(request,'addmission.html',{'posts':posts,'form':form})      

def addmission(request):
    thank = False
    if request.method == 'POST':
      form = AddmissionForm(request.POST)
      if form.is_valid():
        form.save()
        thank = True
      else:
          print('wrong')
          print(form.errors)
    form = AddmissionForm()      
    posts = Enq.objects.all()
    context = {'form':form,'posts':posts, 'thank': thank}
    return render(request,'addmission.html',context)    


def batch(request):
    posts = Batch.objects.latest('batchid')
    posts = posts.batchid
    print(posts)
    thank = False
    if request.method=="POST":
        form = BatchForm(request.POST)
        if form.is_valid():
            form.save()
            thank = True
            sname = []
            print(type(sname))
            sname.append(request.POST.get('sname',''))
            print(sname)
            posts1 = Addmission.objects.all()
            for x in posts1:
                ans = x.add_alias
                print(ans)
                if sname == ans:
                    print(sname)
        else:
            print('wrong')
            print(form.errors)
    newid = posts + 1
    print(newid)
    form = BatchForm(initial={'batchid': newid})             
    context = {'form':form,'posts':posts, 'thank': thank}
    return render(request, 'batch.html', context)

def searchenq(request):
    posts = Enq.objects.all()
    if request.method == 'POST': 
        searchenq = request.POST.get('browsers','')
        print(searchenq)
        posts = Enq.objects.filter(enqalias=searchenq)
    return render(request,'searchenquiry.html',{'posts':posts})

def searchaddmission(request):
    posts = Addmission.objects.all()
    if request.method == 'POST': 
        searchadd = request.POST.get('browsers','')
        print(searchadd)
        posts = Addmission.objects.filter(add_alias=searchadd)
    return render(request,'searchaddmission.html',{'posts':posts})

def searchbatch(request):
    posts = Batch.objects.all()
    if request.method == 'POST': 
        searchbatch = request.POST.get('browsers','')
        print(searchbatch)
        posts = Batch.objects.filter(batchalias=searchbatch)
    return render(request,'searchbatch.html',{'posts':posts})

def Serach_Enq_Alias(request):
    print("select student alias")
    posts = Enq.objects.all()
    if request.method == 'POST': 
        add_alias = request.POST.get('browsers','')
        ans = Enq.objects.filter(enqalias=add_alias)
        for x in ans:
            form = ModifyForm(initial={'enqalias':x.enqalias,'enqid':x.enqid,'fname':x.fname,'lname':x.lname,'email':x.email,
            'phone':x.phone,'Address':x.Address})
    return render(request,'modifyenquiry.html',{'posts':posts,'form':form}) 

def modifyenq(request):
    thank = False
    if request.method == 'POST':
      form = EnquiryForm(request.POST)
      if form.is_valid():
        form.save()
        thank = True
      else:
          print('wrong')
          print(form.errors)
    form = ModifyForm()      
    posts = Enq.objects.all()
    context = {'form':form,'posts':posts, 'thank': thank}
    return render(request,'modifyenquiry.html',context)


def modifyaddmission(request):

    return render(request,'modifyaddmission.html')


def modifybatch(request): 

    return render(request,'modifybatch.html')


def reportenq(request):

    return render(request,'reportenquiry.html')
 


def reportbatch(request):

    return render(request,'reportbatch.html')


def reportcontact(request):

    return render(request,'reportcontact.html')


def feesnew(request):

    return render(request,'feesnew.html')


def feesreport(request): 

    return render(request,'feesreport.html')

def feessearch(request): 

    return render(request,'feessearch.html')    


def internnew(request):

    return render(request,'internnew.html')


def internupdate(request):
    
    return render(request,'internupdate.html')
       