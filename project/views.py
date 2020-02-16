from django.shortcuts import render
from .forms import Enquiry
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
    print('testing')
    thank = False
    if request.method == 'POST':
      form = Enquiry(request.POST)
      if form.is_valid():
        form.save()
        thank = True 
        posts = Enq.objects.values('enqid')[0]
        print(posts)
        newid = int(posts['enqid'])+1
        form = Enquiry(initial={'enqid': newid})
        abc = str(posts.items())
        print(abc)
        value = abc[22]+abc[23]+abc[24]
        print(value)
        ans = Enq.objects.filter(enqid=value).update(enqid=F('enqid') + 1) 
        print(ans)
        form = Enquiry(initial={'enqid':value})
      else:
          print('wrong')
          print(form.errors)
    posts = Enq.objects.values('enqid')[0]
    print(posts)
    newid = int(posts['enqid'])+1
    form = Enquiry(initial={'enqid': newid})
    context = {'form':form,'thank': thank}
    print('hii4')
    return render(request,'enq.html',context)  
    
def createalias(request):
    if request.method=="POST": 
        enqalias = request.POST.get('enqalias','')
    posts = Enq.objects.all() 
    for i in posts:
        if enqalias == str(i):
            context = Enq.objects.get(enqalias=i)
    return render(request, 'addmission.html', {'posts': posts, 'context':context})


def addmission(request):
    posts = Enq.objects.all()
    thank = False
    if request.method=="POST":
        edate = request.POST.get('edate','')
        enqid = request.POST.get('enqid','')
        enqalias = request.POST.get('enqalias','')
        fname = request.POST.get('fname', '')
        lname = request.POST.get('lname', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        Address = request.POST.get('Address', '')
        linux = request.POST.get('linux','off')
        aws = request.POST.get('aws','off')
        python = request.POST.get('python','off')
        devops = request.POST.get('devops','off')
        fullpython = request.POST.get('fullpython','off')
        hadoop = request.POST.get('hadoop','off')
        tot_fees = request.POST.get('tot_fees', '')
        one_install = request.POST.get('one_install','off')
        one_install_date = request.POST.get('one_install_date', '')
        one_install_fees = request.POST.get('one_install_fees', '')
        status = request.POST.get('status','')
        two_install = request.POST.get('two_install','off')
        two_install_date1 = request.POST.get('two_install_date1', '')
        two_install_fees1 = request.POST.get('two_install_fees1', '')
        status1 = request.POST.get('status1','')
        two_install_date2 = request.POST.get('two_install_date2', '')
        two_install_fees2 = request.POST.get('two_install_fees2', '')
        status2 = request.POST.get('status2','')
        three_install = request.POST.get('three_install','off')
        three_install_date1 = request.POST.get('three_install_date1', '')
        three_install_fees1 = request.POST.get('three_install_fees1', '')
        status1 = request.POST.get('status1','')
        three_install_date2 = request.POST.get('three_install_date2', '')
        three_install_fees2 = request.POST.get('three_install_fees2', '')
        status2 = request.POST.get('status2','')
        three_install_date3 = request.POST.get('three_install_date3', '')
        three_install_fees3 = request.POST.get('three_install_fees3', '')
        status3 = request.POST.get('status3','')
        comments = request.POST.get('comments','')
        courses=[]
        if linux == "on":
            courses.append("Linux")
        if aws == "on":
            courses.append("AWS")
        if python == "on":
            courses.append("Python")
        if devops == "on":
            courses.append("Devops")  
        if fullpython == "on":
            courses.append("FullStack") 
        if hadoop == "on":
            courses.append("Hadoop")  
        if one_install == "on":
            one_install_date = one_install_date  
            one_install_fees = one_install_fees
            
        if status == "1":
            status = "Paid"
        if status == "2":
            status = "Not Paid"
        if status == "3":
            status = "Discontinue"     

        if two_install == "on":
            two_install_date1 = two_install_date1  
            two_install_fees1 = two_install_fees1
            two_install_date2 = two_install_date2
            two_install_fees2 = two_install_fees2
        if status1 == "1":
            status1 = "Paid"
        if status1 == "2":
            status1 = "Not Paid"
        if status1 == "3":
            status1 = "Discontinue" 
        if status2 == "1":
            status2 = "Paid"
        if status2 == "2":
            status2 = "Not Paid"
        if status2 == "3":
            status2 = "Discontinue"  

        if three_install == "on":
            three_install_date1 = three_install_date1  
            three_install_fees1 = three_install_fees1
            three_install_date2 = three_install_date2
            three_install_fees2 = three_install_fees2
            three_install_date3 = three_install_date3
            three_install_fees3 = three_install_fees3
        if status1 == "1":
            status1 = "Paid"
        if status1 == "2":
            status1 = "Not Paid"
        if status1 == "3":
            status1 = "Discontinue" 
        if status2 == "1":
            status2 = "Paid"
        if status2 == "2":
            status2 = "Not Paid"
        if status2 == "3":
            status2 = "Discontinue"  
        if status3 == "1":
            status3 = "Paid"
        if status3 == "2":
            status3 = "Not Paid"
        if status3 == "3":
            status3 = "Discontinue"    

        addmission = Addmission(edate = edate, enqalias = enqalias,enqid = enqid, fname = fname, lname = lname, email = email, phone = phone, Address = Address, 
        courses=courses, tot_fees = tot_fees, one_install_date = one_install_date, one_install_fees = one_install_fees, status = status, 
        two_install_date1 = two_install_date1, two_install_fees1 = two_install_fees1, two_install_date2 = two_install_date2, 
        two_install_fees2 = two_install_fees2, three_install_date1 = three_install_date1, three_install_fees1 = three_install_fees1, 
        three_install_date2 = three_install_date2, three_install_fees2 = three_install_fees2, three_install_date3 = three_install_date3, 
        three_install_fees3 = three_install_fees3, status1 = status1, status2 = status2, status3 = status3, comments = comments)
        addmission.save() 
        thank = True 
    return render(request, 'addmission.html', {'posts': posts, 'thank': thank})

def studentdata(request):
    if request.method=="POST": 
        sname = request.POST.get('sname','')
        print(snames)
    posts1 = Addmission.objects.all() 
    for i in posts1:
        if sname == str(i):
            context = Addmission.objects.get(enqalias=i)
            return render(request, 'addmission.html', {'posts1': posts1, 'context':context})


def batch(request):
    posts = Batch.objects.values('batchid')[0]
    print(posts)
    list=[]
    posts1 = Addmission.objects.all()
    thank = False
    if request.method=="POST":
        edate = request.POST.get('edate','') 
        batchid = request.POST.get('batchid','')
        batchalias = request.POST.get('batchalias','')
        trainer_aniket = request.POST.get('trainer_aniket','')
        trainer_yogita = request.POST.get('trainer_yogita','')
        linux = request.POST.get('linux','off')
        aws = request.POST.get('aws','off')
        python = request.POST.get('python','off')
        devops = request.POST.get('devops','off')
        fullpython = request.POST.get('fullpython','off')
        hadoop = request.POST.get('hadoop','off')
        btime = request.POST.get('btime','')
        weekdays = request.POST.get('weekdays','off')
        weekends = request.POST.get('weekends','off')
        days = request.POST.get('days','off')
        specialday = request.POST.get('specialday','') 
        sname =[] 
        sname.append(request.POST.get('list','')) 
        print(sname)
        courses=[]
        if linux == "on":
            courses.append("Linux")
        if aws == "on":
            courses.append("AWS")
        if python == "on":
            courses.append("Python")
        if devops == "on":
            courses.append("Devops")  
        if fullpython == "on":
            courses.append("FullStack") 
        if hadoop == "on":
            courses.append("Hadoop") 
        if weekdays == "on":
            batch_days = "weekdays"
        if weekends == "on":
            batch_days = "weekends"
        if days == "on":
            batch_days = specialday 

        abc = str(posts.items())
        value = abc[24]+abc[25]+abc[26]
        ans = Batch.objects.filter(batchid=value).update(batchid=F('batchid') + 1)
        print(ans)
        trainer = []
        if trainer_aniket == "Aniket":
          batchalias = "B-"+" "+"Aniket"+"_"+str(batchid)
          trainer.append("Aniket") 
          print(batchalias) 
        elif trainer_yogita == "Yogita":
          batchalias = "B-"+" "+"Yogita"+"_"+str(batchid)
          trainer.append("Yogita")
          print(batchalias) 
        
        for i in posts:
          if sname == str(i):
            context = Addmission.objects.get(enqalias=i)
            print(context)        
        batch = Batch(edate = edate,batchid = batchid, batchalias = batchalias, trainer = trainer, courses=courses, batch_time = btime, batch_days = batch_days)
        batch.save()
        thank = True   
    return render(request, 'batch.html', {'posts': posts,'posts1': posts1, 'thank': thank})

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
       