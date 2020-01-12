from django.shortcuts import render
from .models import Enq, Addmission, Batch
from django.http import HttpResponse
from django.utils.dateformat import DateFormat
from django.utils.formats import get_format
from datetime import datetime
from django.db.models import F


# Create your views here

def index(request):
    return render(request,'index.html')
def enq(request):
    l1 =[]
    posts = Enq.objects.values('enqid')[0]
    print(posts)
    print(type(posts))
    
    thank = False
    if request.method=="POST":
        edate = request.POST.get('edate','')
        enqid = request.POST.get('enqid', '')  
        fname = request.POST.get('fname', '')
        l1=[]
        l1.append(fname) 
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
        call = request.POST.get('call','off')
        board = request.POST.get('board','off')
        reference = request.POST.get('reference','off')
        yet5 = request.POST.get('yet5','off')
        f2f = request.POST.get('f2f','off')
        rname = request.POST.get('rname','')
        student = request.POST.get('student','off')
        employee = request.POST.get('employee','off')
        collage = request.POST.get('collage','')
        stream = request.POST.get('stream','')
        fy = request.POST.get('fy','off')
        sy = request.POST.get('sy','off')
        ty = request.POST.get('ty','off')
        passout = request.POST.get('passout','off')
        company = request.POST.get('company','')
        designation = request.POST.get('designation','')
        year_exper = request.POST.get('year_exper','')
        weekdays = request.POST.get('weekdays','off')
        weekend = request.POST.get('weekend','off')
        #both = request.POST.get('both','off')
        wddate = request.POST.get('wddate','')
        weekdays = request.POST.get('weekdays','')
        wedate = request.POST.get('wedate','')
        weekend = request.POST.get('weekend','')
        comments = request.POST.get('comments','')

        courses=[]
        if student == "off":
            collagename = "Null"
            year = "Null"
            stream = "Null"
        if employee == "off":
            company = "Null"
            designation = "Null"
            year_exper = "Null"
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

        if call == "on":
            enquiry = "call"
        elif board == "on":
            enquiry = "Board"
        elif yet5 == "on":
            enquiry = "yet5"
        elif f2f == "on":
            enquiry = "Face to face"
        elif reference == "on":
            enquiry = rname

        if student == "on":
            collagename = collage
            stream = stream  
            if fy == "on":
                year = "First Year" 
            if sy == "on":
                year = "Second Year"
            if ty == "on":
                year = "Thrid Year"
            if passout == "on":
                year = "pass Out"  
        if employee == "on":
            company = company
            designation = designation  
            year_exper = year_exper 

        if weekdays == "on": 
            wddate = wddate
            weekdays = weekdays
        if weekdays == "on": 
            wedate = wedate
            weekend = weekend
        l1=[]
        l1.append(fname)    
        posts1 = Enq.objects.values('enqid')
        ans = posts1.update(enqid=F('enqid') + 1)
        print(ans)
        
        eid = int(enqid)
        print(eid)
        print(type(eid))
        eid += 1 
        print(eid)
        enqalias = fname+lname[0:2]+str(eid)
        print(enqalias)        
        enq = Enq(edate=edate,enqalias = enqalias ,enqid = eid, fname=fname, lname=lname, email=email, phone=phone, Address=Address, courses=courses, enquiry=enquiry, 
        collagename = collagename, stream=stream, year=year, company = company, designation = designation, year_exper = year_exper, 
        weekday_date = wddate, weekdays = weekdays, weekend_date = wedate, weekend = weekend, comments = comments)
        enq.save() 
        thank = True 
    return render(request, 'enq.html', {'posts': posts, 'thank': thank})
    
  
def addmission(request):
    thank = False
    if request.method=="POST":
        edate = request.POST.get('edate','')     
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

        addmission = Addmission(edate = edate, fname = fname, lname = lname, email = email, phone = phone, Address = Address, 
        courses=courses, tot_fees = tot_fees, one_install_date = one_install_date, one_install_fees = one_install_fees, status = status, 
        two_install_date1 = two_install_date1, two_install_fees1 = two_install_fees1, two_install_date2 = two_install_date2, 
        two_install_fees2 = two_install_fees2, three_install_date1 = three_install_date1, three_install_fees1 = three_install_fees1, 
        three_install_date2 = three_install_date2, three_install_fees2 = three_install_fees2, three_install_date3 = three_install_date3, 
        three_install_fees3 = three_install_fees3, status1 = status1, status2 = status2, status3 = status3, comments = comments)
        addmission.save() 
        thank = True 
    return render(request, 'addmission.html', {'thank': thank})

def batch(request):
    thank = False
    if request.method=="POST":
        edate = request.POST.get('edate','') 
        trainer_aniket = request.POST.get('trainer_aniket','off')
        trainer_yogita = request.POST.get('trainer_yogita','off')
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
        sname = request.POST.get('sname','')
        B_student = Addmission.objects.get(fname = sname)
        print(B_student)
        if trainer_aniket == "on":
            trainer = "trainer_aniket"
        if trainer_yogita == "on":
            trainer = "trainer_yogita"
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

        batch = Batch(edate = edate, trainer = trainer, courses=courses, batch_time = btime, batch_days = batch_days)

        batch.save()
        thank = True
        return render(request, 'batch.html', {'thank':thank, 'B_student': B_student})

    return render(request, 'batch.html', {'thank': thank})