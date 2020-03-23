from django import forms
from .models import Enq , Addmission , Batch 


# Create your models here.

class Enquiry(forms.ModelForm):
    
    choices = (
    ('linux', 'Linux'),('aws', 'AWS(Cloud)'),('python', 'Python'),('devops', 'DevOps'),('fullpython', 'FullStack(Python)'),('hadoop', 'HadoopAdmin'),
    )
    enquiry_choices = (
    ('call', 'Call'),('board', 'Board'),('reference', 'Reference'),('yet5', 'Yet5'),('f2f', 'Face-2-Face'),
    )
    status_choices = (
    ('student', 'Student'),('employee', 'Employee'),
    )
    year_choices = (
    ('fy', 'FY'),('sy', 'SY'),('ty', 'TY'),('passout', 'PassOut'),
    )
    preferred_choices = (
    ('weekdays', 'Weekdays'),('weekend', 'Weekend'),
    )
    courses = forms.MultipleChoiceField(choices=choices, widget=forms.CheckboxSelectMultiple(attrs={'class': 'inline'}))
    enquiry = forms.ChoiceField(choices=enquiry_choices, widget=forms.RadioSelect(attrs={'class': 'inline' , 'onclick' : "ShowHideDiv()"}))
    status = forms.ChoiceField(choices=status_choices, widget=forms.RadioSelect(attrs={'class': 'inline' , 'onclick' : "ShowHideDiv()"}))
    year = forms.ChoiceField(required=False, choices=year_choices,  widget=forms.RadioSelect(attrs={'class': 'inline'}))
    Preferred_day = forms.ChoiceField(choices=preferred_choices, widget=forms.RadioSelect(attrs={'class': 'inline' , 'onclick' : "ShowHideDiv()"}))

    class Meta:
        model = Enq
        fields = '__all__'
        widgets = {
            'edate': forms.DateInput(
                attrs={ 'style' : 'margin-right: 15.25em' , 'id' : "edate" ,  'type' : "date" , 'class' : "form-check-label"}),
            'enqalias': forms.TextInput(
                attrs={ 'id' : "enqalias" , 'style' : 'margin-right: 15.25em' , 'name' : "enqalias"}), 
            'enqid': forms.TextInput(
                attrs={'id' : "enqid" , 'name':"enqid" , 'value':'{{ form.enqid.value }}', 'style' : 'margin-right: 15.25em' }), 
            'fname': forms.TextInput(
                attrs={ 'class':"form-control col-md-08 fname" , 'id':"fname" , 'placeholder':"First Name"}),
            'lname': forms.TextInput(
                attrs={ 'class':"form-control col-md-08" , 'id':"lname" , 'placeholder':"Last Name"}), 
            'email': forms.EmailInput(
                attrs={'id':"email" , 'placeholder':"Email Address" , 'class':"form-control col-md-12"}), 
            'phone': forms.NumberInput(
                attrs={ 'id':"phone" , 'placeholder' : "Phone Number" , 'class' : "form-control col-md-12"}),
            'Address': forms.TextInput(
                attrs={ 'class':"form-control col-md-12" , 'id':"Address" , 'placeholder':"Address" , 'rows':"3"}), 
            'reference_name': forms.TextInput(
                attrs={ 'class':"form-control Reference Name" , 'id' : "reference_name" , 'placeholder' : "Reference Name"}),
            'collagename': forms.TextInput(
                attrs={ 'class' : "form-control collegename" , 'id' : "college" , 'placeholder' : "College Name"}), 
            'stream': forms.TextInput(
                attrs={ 'class' : "form-control stream" , 'id' : "stream" , 'placeholder' : "Stream(BCA,BCS,BTech)..." }), 
            'company': forms.TextInput(
                attrs={ 'class' : "form-control" , 'id' : "company" , 'placeholder' : "Company Name"}), 
            'designation': forms.TextInput(
                attrs={ 'class' : "form-control" , 'id' : "designation" , 'placeholder' : "Designation"}), 
            'year_exper': forms.TextInput(
                attrs={ 'class' : "form-control" , 'id' : "years_of_exper" , 'placeholder' : "No. of Years of Experience"}), 
            'weekday_date': forms.DateInput(
                attrs={ 'style' : 'margin-right: 15.25em' , 'type': 'date' , 'id' : "wddate" , 'class' : "form-check-label"}), 
            'weekdays_time': forms.TextInput(
                attrs={ 'class' : "form-control weekdaystime" , 'id' : "preweekdays" , 'placeholder' : "Preferred Time For Weekdays"}), 
            'weekend_date': forms.DateInput(
                attrs={ 'style' : 'margin-right: 15.25em' , 'type': 'date' , 'id' : "wedate" , 'class' : "form-check-label"}), 
            'weekend_time': forms.TextInput(
                attrs={ 'class' : "form-control weekendtime" , 'id' : "preweekend" , 'placeholder' : "Preferred Time For Weekend"}),  
            'comments' : forms.Textarea(
                attrs={ 'class' : "form-control col-md-12" , 'id' : "comments" , 'placeholder' : "Comments" , 'rows' : "3"}),                       
        }
        

class AddmissionForm(forms.ModelForm):
    choices = (
    ('linux', 'Linux'),('aws', 'AWS(Cloud)'),('python', 'Python'),('devops', 'DevOps'),('fullpython', 'FullStack(Python)'),('hadoop', 'HadoopAdmin'),
    )
    pay_fees = (
    ('one_install', 'One Installment'),('two_install', 'Two Installment'),('three_install', 'Three Installment'),
    )
    status = (
    ('Paid', 'Paid'),('Not Paid', 'Not Paid'),('Discontinue', 'Discontinue'),
    )
    courses = forms.MultipleChoiceField(choices=choices, widget=forms.CheckboxSelectMultiple(attrs={'class': 'inline'}))
    pay_fees = forms.ChoiceField(choices=pay_fees, widget=forms.RadioSelect(attrs={'class': 'inline' , 'onclick' : "ShowHideDiv()"}))
    status = forms.Select(choices=status)
    
    class Meta:
        status = (
        ('Paid', 'Paid'),('Not Paid', 'Not Paid'),('Discontinue', 'Discontinue'),
        )
        model = Addmission
        fields = '__all__'
        widgets = {
            'add_date': forms.DateInput(
                attrs={'style' : 'margin-right: 15.25em','id':"add_date" , 'name':"add_date" , 'type':"date"}),
            'add_alias': forms.TextInput(
                attrs={ 'id':"enqalias" , 'name':"enqalias",'style' : 'margin-right: 15.25em'}), 
            'add_id': forms.TextInput(
                attrs={ 'id':"add_id" , 'name':"add_id",'style' : 'margin-right: 15.25em'}), 
            'fname': forms.TextInput(
                attrs={ 'id':"fname" , 'name':"fname", 'placeholder':"First Name" , 'class':"form-control col-md-08"}),
            'lname': forms.TextInput(
                attrs={ 'id':"lname" , 'name':"lname" , 'placeholder':"Last Name" , 'class':"form-control col-md-08"}), 
            'email': forms.EmailInput(
                attrs={'id':"email" , 'name':"email" , 'placeholder':"Email Address" , 'class':"form-control col-md-12"}), 
            'phone': forms.NumberInput(
                attrs={ 'id':"phone" , 'name':"phone"  , 'placeholder':"Phone" , 'class':"form-control col-md-12"}),
            'Address': forms.TextInput(
                attrs={ 'class':"form-control col-md-12" , 'id':"Address" , 'name':"Address" , 'placeholder':"Address" , 'rows':"3"}), 
            'tot_fees': forms.NumberInput(
                attrs={ 'id':"tot_fees" , 'name':"tot_fees" , 'placeholder':"Total Fess"}), 
            'one_install_date': forms.DateInput(
                attrs={ 'id':"one_install_date" , 'name':"one_install_date", 'type':"date" , 'class':"resizedTextbox"}), 
            'one_install_fees': forms.TextInput(
                attrs={ 'name':"one_install_fees" , 'placeholder':"Enter fees" , 'class':"resizedTextbox"}), 
            'status': forms.Select(choices=status , attrs={'class':"resizedTextbox" , 'name':"status" , 'id':"status"}),
            'two_install_date1': forms.DateInput(
                attrs={ 'id':"two_install_date1" , 'name':"two_install_date1", 'type':"date" , 'class':"resizedTextbox"}), 
            'two_install_fees1': forms.TextInput(
                attrs={ 'name':"two_install_fees1" , 'placeholder':"Enter fees" , 'class':"resizedTextbox"}), 
            'two_install_date2': forms.DateInput(
                attrs={ 'id':"two_install_date2" , 'name':"two_install_date2", 'type':"date" , 'class':"resizedTextbox"}),
            'two_install_fees2': forms.TextInput(
                attrs={ 'name':"two_install_fees2" , 'placeholder':"Enter fees" , 'class':"resizedTextbox"}), 
            'three_install_date1': forms.DateInput(
                attrs={ 'id':"three_install_date1" , 'name':"three_install_date1", 'type':"date" , 'class':"resizedTextbox"}), 
            'three_install_fees1': forms.TextInput(
                attrs={ 'name':"three_install_fees1" , 'placeholder':"Enter fees" , 'class':"resizedTextbox"}), 
            'three_install_date2': forms.DateInput(
                attrs={ 'id':"three_install_date2" , 'name':"three_install_date2", 'type':"date" , 'class':"resizedTextbox"}), 
            'three_install_fees2': forms.TextInput(
                attrs={ 'name':"three_install_fees2" , 'placeholder':"Enter fees" , 'class':"resizedTextbox"}),                                             
            'three_install_date3' : forms.DateInput(
                attrs={ 'id':"three_install_date3" , 'name':"three_install_date3", 'type':"date" , 'class':"resizedTextbox"}),
            'three_install_fees3' : forms.TextInput(
                attrs={ 'name':"three_install_fees3" , 'placeholder':"Enter fees" , 'class':"resizedTextbox"}),  
            'status1' : forms.Select(choices=status , attrs={'class':"resizedTextbox" , 'name':"status1" , 'id':"status1"}),
            'status2' : forms.Select(choices=status , attrs={'class':"resizedTextbox" , 'name':"status2" , 'id':"status2"}),   
            'status3' : forms.Select(choices=status , attrs={'class':"resizedTextbox" , 'name':"status3" , 'id':"status3"}),
            'comments' : forms.Textarea(
                attrs={ 'class' : "form-control col-md-12" , 'id' : "comments" , 'placeholder' : "Comments" , 'rows' : "3"}),                                        
        }  

class BatchForm(forms.ModelForm):
    trainer_choices = (
    ('trainer_aniket', 'Aniket'),('trainer_yogita', 'Yogita'),
    )
    choices = (
    ('linux', 'Linux'),('aws', 'AWS(Cloud)'),('python', 'Python'),('devops', 'DevOps'),('fullpython', 'FullStack(Python)'),('hadoop', 'HadoopAdmin'),
    )
    day_choices = (
    ('weekdays', 'Weekdays'),('weekends', 'Weekends'),('other','special_day')
    )
    trainer = forms.ChoiceField(choices=trainer_choices, widget=forms.RadioSelect(attrs={'class': 'inline', 'onclick': "myFunction(this.value)"}))
    courses = forms.MultipleChoiceField(choices=choices, widget=forms.CheckboxSelectMultiple(attrs={'class': 'inline'}))
    batch_day = forms.ChoiceField(choices=day_choices, widget=forms.RadioSelect(attrs={'class': 'inline'}))
    sname = forms.ModelMultipleChoiceField(queryset=Addmission.objects.all())
    class Meta:
        choices1 = (
        ('linux', 'Linux'),('aws', 'AWS(Cloud)'),('python', 'Python'),('devops', 'DevOps'),('fullpython', 'FullStack(Python)'),('hadoop', 'HadoopAdmin'),
        )
        model = Batch
        fields = '__all__'
        widgets = {
            'edate': forms.DateInput(
                attrs={ 'style' : 'margin-right: 10.25em' , 'id':"edate" , 'name':"edate" , 'type':"date" , 'class':"form-check-label"}),
            'batchid': forms.TextInput(
                attrs={ 'id':"batchid" , 'name':"batchid" , 'value':"{{ form.batchid.value }}"}), 
            'batchalias': forms.TextInput(
                attrs={ 'id':"batchalias" ,'style' : 'margin-right: 10.25em' , 'name':"batchalias"}), 
            'batch_time': forms.TimeInput(
                attrs={'name':"batch_time" , 'id':"batch_time"}),
            'special_day': forms.TextInput(
                attrs={ 'placeholder':"SpecificDays" , 'style':'margin-right: 5.25em' , 'class':"form-check-label" , 'for':"other" , 'name':"special_day"}),  
            'sname' : forms.Select(
                attrs={'class':"selectpicker" , 'multiple data-live-search':"true"}), 
        }

class searchbatchForm(forms.Form):
    CHOICES=[('modify','Modify Batch'),('delete','Delete Batch')]    
    like1 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(attrs={'class': 'inline'}))       

class reportenqForm(forms.Form):
    CHOICES=[('all_enq','All-Enquiries'),('today','Today'),('yesterday','Yesterday'),('current_week','Current_Week'),
         ('current_month','Current_Month'),('not_converted','not_converted')]
    select = (
        ('01', 'January'),('02', 'Febuary'),('03', 'March'),('04', 'April'),('05', 'May'),('06', 'June'),('07', 'July'),('08', 'August'),
        ('09', 'September'),('10', 'October'),('11', 'November'),('12', 'December'),
        )     

    like = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(attrs={'class': 'inline'}))
    select = forms.ChoiceField(choices = select)
    
class reportbatchForm(forms.Form):
    CHOICES=[('trainer_aniket','Aniket'),('trainer_yogita','Yogita')]
    select = [('complete', 'Completed'),('on_going', 'On-Going')]
        
    trainer = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(attrs={'class': 'inline'}))
    select = forms.ChoiceField(choices=select, widget=forms.RadioSelect(attrs={'class': 'inline'})) 

class reportcontactForm(forms.Form):
    select = (
    ('first_name', 'First Name'),('last_name', 'Last Name'),('student_alias', 'Student Alias'),
    )
 
    select = forms.ChoiceField(choices=select, widget=forms.RadioSelect(attrs={'class': 'inline' , 'onclick' : "ShowHideDiv()"})) 
    fname = forms.CharField(max_length=100, required=False, widget=forms.TextInput(
        attrs={'style':'margin-right: 3.25em', 'name':"fname", 'placeholder':"Student First Name", 'class':"resizedTextbox"}))
    lname = forms.CharField(max_length=100, required=False, widget=forms.TextInput(
        attrs={'style':'margin-right: 3.25em', 'name':"lname", 'placeholder':"Student Last Name", 'class':"resizedTextbox"}))  
    alias = forms.CharField(max_length=100, required=False, widget=forms.TextInput(
        attrs={'style':'margin-right: 3.25em', 'name':"alias", 'placeholder':"Enquiry Alias Name", 'class':"resizedTextbox"}))    
    