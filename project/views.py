from django.shortcuts import render
from .forms import Enquiry, AddmissionForm, BatchForm
from .models import Enq, Addmission, Batch
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
        else:
            print('wrong')
            print(form.errors)
    newid = posts + 1
    print(newid)
    form = BatchForm(initial={'batchid': newid})             
    context = {'form':form,'posts':posts, 'thank': thank}
    return render(request, 'batch.html', context)

def searchenq(request):

    return render(request,'searchenquiry.html')

def searchaddmission(request):

    return render(request,'searchaddmission.html')

def searchbatch(request):

    return render(request,'searchbatch.html')


def modifyenq(request):

    return render(request,'modifyenquiry.html')


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
       