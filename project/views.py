from django.shortcuts import render, redirect
from .forms import Enquiry, AddmissionForm, BatchForm, reportenqForm, searchbatchForm, reportbatchForm, reportcontactForm
from .models import Enq, Addmission, Batch
from django.http import HttpResponse, JsonResponse
from django.utils.dateformat import DateFormat
from django.utils.formats import get_format
from datetime import datetime, timedelta
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
    posts2 = Addmission.objects.all()
    print(posts2)
    for i in posts2:
        print(i.fname)
        print(i.E_id.enqalias)
        print(i.add_alias)
    print("select student alias")
    posts = Enq.objects.all()
    if request.method == 'POST': 
        add_alias = request.POST.get('browsers','')
        ans = Enq.objects.filter(enqalias=add_alias)
        for x in ans:
            a=x.fname.capitalize()
            b=x.lname[0:2].capitalize()
            alias="A- "+a+"_"+b+str(x.enqid)
            print(alias)
            print(x.courses)
            a=x.courses
            punc = '''[]'"\< >'''
            analyzed = ""
            for char in a:
                if char not in punc:
                    analyzed=analyzed+char
            a1=analyzed.split(',')
            print(a1)
            form = AddmissionForm(initial={'add_date':x.edate,'add_alias':alias,'add_id':x.enqid,'fname':x.fname,'lname':x.lname,'email':x.email,
            'phone':x.phone,'Address':x.Address,'courses':a1})
            print(form)
    return render(request,'addmission.html',{'posts':posts,'form':form})      

def addmission(request):
    thank = False
    posts = Enq.objects.all()
    if request.method == 'POST':
        form = AddmissionForm(request.POST)
        print(form)
        if form.is_valid():
            print("HIII")
            form.save()
            thank = True
        else:
            print('wrong')
            print(form.errors)
    else:
        form = AddmissionForm()
    return render(request,'addmission.html',{'form':form,'posts':posts, 'thank': thank})    


def batch(request):
    posts = Batch.objects.latest('batchid')
    posts = posts.batchid
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
            print(x.courses)
            a=x.courses
            punc = '''[]'"\< >'''
            analyzed = ""
            for char in a:
                if char not in punc:
                    analyzed=analyzed+char
            a1=analyzed.split(',')
            print(a1)
            form = Enquiry(initial={'edate':x.edate, 'enqalias':x.enqalias,'enqid':x.enqid,'fname':x.fname,'lname':x.lname,'email':x.email,
            'phone':x.phone,'Address':x.Address,'courses':a1,'enquiry':x.enquiry,'reference_name':x.reference_name,'status':x.status,
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
    print("hiii")
    print("select student alias")
    posts = Addmission.objects.all()
    if request.method == 'POST': 
        add_alias = request.POST.get('browsers','')
        print(add_alias)
        ans = Addmission.objects.filter(add_alias=add_alias)
        for x in ans:
            print(x.courses)
            a=x.courses
            b=x.add_alias
            alias="E-"+b[2:]
            punc = '''[]'"\< >'''
            analyzed = ""
            for char in a:
                if char not in punc:
                    analyzed=analyzed+char
            a1=analyzed.split(',')
            form = AddmissionForm(initial={'E_id':alias,'add_date':x.add_date, 'add_alias':x.add_alias,'add_id':x.add_id,'fname':x.fname,'lname':x.lname,'email':x.email,'phone':x.phone,
            'Address':x.Address,'courses':a1,'tot_fees':x.tot_fees,'pay_fees':x.pay_fees,'one_install_date':x.one_install_date,'one_install_fees':x.one_install_fees,
            'status':x.status,'two_install_date1':x.two_install_date1,'two_install_fees1':x.two_install_fees1,'two_install_date2':x.two_install_date2,'two_install_fees2':x.two_install_fees2,
            'three_install_date1':x.three_install_date1,'three_install_fees1':x.three_install_fees1,'three_install_date2':x.three_install_date2,'three_install_fees2':x.three_install_fees2,
            'three_install_date3':x.three_install_date3,'three_install_fees3':x.three_install_fees3,'status1':x.status1,'status2':x.status2,'status3':x.status3,'comments':x.comments})                    
    return render(request,'modifyaddmission.html',{'posts':posts,'form':form}) 

def modifyaddmission(request):
    thank = False
    if request.method == 'POST':
      add_id = request.POST.get('add_id','')
      print(add_id)
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
        form1 =searchbatchForm(request.POST)
        if form1.is_valid():
            cd = form1.cleaned_data
            print(cd)
            cd=str(cd)
            operation=cd[11:-2]
        if operation == "modify":
            ans = Batch.objects.filter(batchalias=batchalias)
            for x in ans:
                a=x.courses
                punc = '''[]'"\< >:'''
                analyzed = ""
                for char in a:
                    if char not in punc:
                        analyzed=analyzed+char
                a1=analyzed.split(',')
                form = BatchForm(initial={'edate':x.edate, 'batchid':x.batchid,'batchalias':x.batchalias,'trainer':x.trainer,'courses':a1,
                'batch_time':x.batch_time,'batch_day':x.batch_day,'special_day':x.special_day})   
        elif operation == "delete":  
            ans = Batch.objects.filter(batchalias=batchalias).delete()
            print("record is deleted")   
            return redirect('/modifybatch/')  
    form1 =searchbatchForm()      
    return render(request,'modifybatch.html',{'posts':posts,'form':form,'form1':form1}) 

def modifybatch(request):
    sname = [] 
    select=[]
    print("HIIII123") 
    thank = False
    if request.method == 'POST':
        batchid = request.POST.get('batchid','')
        update = Batch.objects.get(batchid=batchid)
        t1=tuple()
        for z in update:
            a=z[1]
            t1 = t1 + (a,)
        print(t1[-1])  
        select.append(t1[-1])  
        form = BatchForm(request.POST, instance=update)
        if form.is_valid():
            cd = form.cleaned_data
            print(cd)
            stud_add = request.POST.get('stud_add','off')
            print(stud_add)
            stud_remove = request.POST.get('stud_remove','off')
            print(stud_remove)
            for q,j in cd.items():
                select.append(j)
            a=list(select[8])
            print(a)
            for i in a:
                print(i)
            sname.append(request.POST.get('sname',''))
            posts1 = Addmission.objects.all()
            for x in posts1:
                ans = x.add_alias
                if sname == ans:
                    print(sname)       
            form.save()
            thank = True
        else:
            print('#######____ERROR_____##########')
            print(form.errors)
    form = BatchForm()  
    form1 =searchbatchForm()     
    posts = Batch.objects.all()
    context = {'form':form,'form1':form1,'posts':posts, 'thank': thank}
    return render(request,'modifybatch.html',context)
 
def reportenq(request):
    select=[]
    a1=[]
    if request.method == 'POST':
        form = reportenqForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            for q,j in cd.items():
                select.append(j)
                if j == "all_enq":
                    ans = Enq.objects.values('edate')
                    for i in ans:
                        a=str(i)
                        year,month,day=a.split('-')
                        if select[0] == month:
                            date=a[11:21]
                            record = Enq.objects.filter(edate=date)
                            a1.append(record) 
                if j == "today":
                    cur_date=datetime.date(datetime.now())
                    ans = Enq.objects.values('edate')
                    for i in ans:
                        a=str(i)
                        date=a[11:21]  
                        if date == str(cur_date):
                            record = Enq.objects.filter(edate=date)
                            a1.append(record)    
                if j == "yesterday":
                    yesterday = datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d')
                    ans = Enq.objects.values('edate')
                    for i in ans:
                        a=str(i)
                        date=a[11:21]  
                        if date == str(yesterday):
                            record = Enq.objects.filter(edate=date)
                            a1.append(record) 
                if j == "current_week":
                    Jan1st = datetime.date(datetime.now())
                    year,week_num,day_of_week = Jan1st.isocalendar() 
                    ans = Enq.objects.values('edate')
                    for i in ans:
                        a=str(i)
                        date1=a[11:21] 
                        datetime_object = datetime.strptime(date1, '%Y-%m-%d')
                        year1,week_num1,day_of_week1 = datetime_object.isocalendar() 
                        if week_num1 == week_num:
                            record = Enq.objects.filter(edate=date1)
                            a1.append(record)      
                if j == "current_month":
                    d = datetime.date(datetime.now())
                    m='%02d' % d.month
                    ans = Enq.objects.values('edate')
                    for i in ans:
                        a=str(i)
                        year,month,day=a.split('-')
                        if m == month:
                            date=a[11:21]
                            record = Enq.objects.filter(edate=date)
                            a1.append(record)   
                if j == "not_converted":
                    studenq = Enq.objects.values('enqalias')
                    studadd = Addmission.objects.values('add_alias')
                    list1=[]
                    list2=[]
                    ans=set()
                    for i in studenq:
                        a=str(i)
                        a=a[17:-2]
                        list1.append(a)
                        print(list1)
                    for i in studadd:
                        b=str(i)
                        b=b[18:-2]
                        list2.append(b)
                        print(list2)
                    for i in list1:
                        for j in list2:
                            ans.update([i])
                            if str(i) == str(j):
                                ans.remove(i)
                                break
                            else:
                                ans.update([i])
                    print(ans)  
                    for i in ans:
                        alias="E- "+i
                        print(alias)
                        record = Enq.objects.filter(enqalias=alias)
                        a1.append(record)  
                        print(a1)                     
    else:
        form = reportenqForm()
    return render(request,'reportenquiry.html', {'form':form,'a1':a1})



def reportbatch(request):
    if request.method == 'POST':
        form = reportbatchForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            a=cd['select']
            b=cd['trainer']
            if a == "complete":
                record=Batch.objects.filter(trainer=b,complete='True')
                print(record)
                ans=[]
                for i in record:
                    print(i.batchid)
                    print(i.batchalias)
                    print(i.Addmission.all()) 
                    ans = i.Addmission.all()
                    for x in ans:
                        print(x.fname)
                        print(x.add_alias)
                        print(x.phone)
                        print(x.email)
                        context = {'form':form,'ans':ans,'record':record} 
                context = {'form':form,'ans':ans,'record':record} 
            elif a == "on_going":
                record=Batch.objects.filter(trainer=b,complete='False')
                print(record)
                ans=[]
                for i in record:
                    print(i.batchid)
                    print(i.batchalias)
                    print(i.Addmission.all()) 
                    ans1 = i.Addmission.all()
                    list1=[]
                    for x in ans1:
                        list1.append(x) 
                        print(list1)
                    ans.append(list1)
                    print(ans)
                    context = {'form':form,'ans':ans,'record':record} 
                    for z in ans:
                        print(z)
                        for x in z:
                            print(x.fname)
                            print(x.lname)
    else:
        form = reportbatchForm() 
        context = {'form':form}   
    return render(request,'reportbatch.html',context)


def reportcontact(request):
    thank = False
    if request.method == 'POST':
        form = reportcontactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            b=cd['fname'].lower()
            b1=cd['lname'].lower()
            b2=cd['alias']
            if b != '':
                ans=Enq.objects.filter(fname=b)
                ans1=Addmission.objects.filter(fname=b)
                for i in ans1:
                    xyz = i.add_id
                    print(xyz) 
                ans2=Batch.objects.all()
                context = {'form':form, 'ans': ans, 'ans1':ans1,'ans2':ans2}
                return render(request,'reportcontact.html',context)
                for field in Batch.objects.all():
                    ans3=field.Addmission.all()
                    for x in ans1:
                        for i in ans3:
                            if i == x:
                                print(i)  
                                print(field.batch_time) 
                                print(field.batch_day) 
                                print(field.special_day) 
                                   
            elif b1 != '':    
                ans=Enq.objects.filter(lname=b1)
                print(ans)
            elif b2 !='':    
                ans=Enq.objects.filter(enqalias=b2)
                print(ans)
            
        else:
            print('#######____ERROR_____##########')
            print(form.errors)
    form = reportcontactForm()      
    context = {'form':form}
    return render(request,'reportcontact.html',context)


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
       