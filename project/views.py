from django.shortcuts import render, redirect
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
        studalias = request.POST.get('browsers','')
        ans = Enq.objects.filter(enqalias=studalias)
        for x in ans:
            form = Enquiry(initial={'edate':x.edate, 'enqalias':x.enqalias,'enqid':x.enqid,'fname':x.fname,'lname':x.lname,'email':x.email,
            'phone':x.phone,'Address':x.Address,'courses':x.courses,'enquiry':x.enquiry,'reference_name':x.reference_name,'status':x.status,
            'collagename':x.collagename,'stream':x.stream,'year':x.year,'company':x.company,'designation':x.designation,'year_exper':x.year_exper,
            'Preferred_day':x.Preferred_day,'weekday_date':x.weekday_date,'weekdays_time':x.weekdays_time,'weekend_date':x.weekend_date,
            'weekend_time':x.weekend_time,'comments':x.comments})           
    return render(request,'modifyenquiry.html',{'posts':posts,'form':form}) 

def modifyenq(request):
    thank = False
    if request.method == 'POST':
      enqid = request.POST.get('enqid','')
      update = Enq.objects.get(enqid=enqid)
      form = Enquiry(request.POST, instance=update)
      if form.is_valid():
        form.save()
        thank = True
      else:
          print('#######____ERROR_____##########')
          print(form.errors)
    form = Enquiry()      
    posts = Enq.objects.all()
    context = {'form':form,'posts':posts, 'thank': thank}
    return render(request,'modifyenquiry.html',context)

def Serach_Addmission_Alias(request):
    print("select student alias")
    posts = Addmission.objects.all()
    if request.method == 'POST': 
        add_alias = request.POST.get('browsers','')
        ans = Addmission.objects.filter(add_alias=add_alias)
        for x in ans:
            form = AddmissionForm(initial={'add_date':x.add_date, 'add_alias':x.add_alias,'add_id':x.add_id,'fname':x.fname,'lname':x.lname,'email':x.email,'phone':x.phone,
            'Address':x.Address,'courses':x.courses,'tot_fees':x.tot_fees,'pay_fees':x.pay_fees,'one_install_date':x.one_install_date,'one_install_fees':x.one_install_fees,
            'status':x.status,'two_install_date1':x.two_install_date1,'two_install_fees1':x.two_install_fees1,'two_install_date2':x.two_install_date2,'two_install_fees2':x.two_install_fees2,
            'three_install_date1':x.three_install_date1,'three_install_fees1':x.three_install_fees1,'three_install_date2':x.three_install_date2,'three_install_fees2':x.three_install_fees2,
            'three_install_date3':x.three_install_date3,'three_install_fees3':x.three_install_fees3,'status1':x.status1,'status2':x.status2,'status3':x.status3,'comments':x.comments})              
    return render(request,'modifyaddmission.html',{'posts':posts,'form':form}) 

def modifyaddmission(request):
    thank = False
    if request.method == 'POST':
      add_id = request.POST.get('add_id','')
      update = Addmission.objects.get(add_id=add_id)
      form = AddmissionForm(request.POST, instance=update)
      if form.is_valid():
        form.save()
        thank = True
      else:
          print('#######____ERROR_____##########')
          print(form.errors)
    form = AddmissionForm()      
    posts = Addmission.objects.all()
    context = {'form':form,'posts':posts, 'thank': thank}
    return render(request,'modifyaddmission.html',context)

def Serach_Batch_Alias(request):
    print("select Batch alias")
    posts = Batch.objects.all()
    if request.method == 'POST':
        print("HIIII") 
        batchalias = request.POST.get('browsers','')
        modify = request.POST.get('modify','off')
        delete = request.POST.get('delete','off')
        print(batchalias)
        print(modify)
        print(delete)
        if modify == "on":
            ans = Batch.objects.filter(batchalias=batchalias)
            for x in ans:
                form = BatchForm(initial={'edate':x.edate, 'batchid':x.batchid,'batchalias':x.batchalias,'trainer':x.trainer,'courses':x.courses,
                'batch_time':x.batch_time,'batch_time':x.batch_time,'special_day':x.special_day,'sname':x.sname})   
        elif delete == "on":  
            ans = Batch.objects.filter(batchalias=batchalias).delete()
            print("record is deleted")   
            return redirect('/modifybatch/')         
    return render(request,'modifybatch.html',{'posts':posts,'form':form}) 

def modifybatch(request): 
    thank = False
    if request.method == 'POST':
      batchid = request.POST.get('batchid','')
      update = Batch.objects.get(batchid=batchid)
      form = BatchForm(request.POST, instance=update)
      if form.is_valid():
        form.save()
        thank = True
      else:
          print('#######____ERROR_____##########')
          print(form.errors)
    form = BatchForm()      
    posts = Batch.objects.all()
    context = {'form':form,'posts':posts, 'thank': thank}
    return render(request,'modifybatch.html',context)
 


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
       