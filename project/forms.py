from django import forms
from .models import Enq



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
    year = forms.ChoiceField(choices=year_choices, widget=forms.RadioSelect(attrs={'class': 'inline'}))
    Preferred_day = forms.ChoiceField(choices=preferred_choices, widget=forms.RadioSelect(attrs={'class': 'inline' , 'onclick' : "ShowHideDiv()"}))
    class Meta:
        model = Enq
        fields = '__all__'
        widgets = {
            'edate': forms.DateInput(
                attrs={ 'style' : 'margin-right: 15.25em' , 'id' : "edate" ,  'type' : "date" , 'class' : "form-check-label"}),
            'enqid': forms.TextInput(
                attrs={ 'id' : "enqid" , 'value' : "{{ posts.enqid }}"}), 
            'fname': forms.TextInput(
                attrs={ 'class':"form-control col-md-08 fname" , 'id':"fname" , 'placeholder':"First Name"}),
            'lname': forms.TextInput(
                attrs={ 'class':"form-control col-md-08" , 'id':"lname" , 'placeholder':"Last Name"}), 
            'enqalias': forms.TextInput(
                attrs={ 'id' : "enqalias" , 'style' : 'margin-right: 15.25em' , 'name' : "enqalias"}), 
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
                attrs={ 'style' : 'margin-right: 20.25em' , 'type': 'date' , 'id' : "wddate" , 'class' : "form-check-label"}), 
            'weekdays_time': forms.TextInput(
                attrs={ 'class' : "form-control weekdaystime" , 'id' : "preweekdays" , 'placeholder' : "Preferred Time For Weekdays"}), 
            'weekend_date': forms.DateInput(
                attrs={ 'style' : 'margin-right: 20.25em' , 'type': 'date' , 'id' : "wedate" , 'class' : "form-check-label"}), 
            'weekend_time': forms.TextInput(
                attrs={ 'class' : "form-control weekendtime" , 'id' : "preweekend" , 'placeholder' : "Preferred Time For Weekend"}),  
            'comments' : forms.Textarea(
                attrs={ 'class' : "form-control col-md-12" , 'id' : "comments" , 'placeholder' : "Comments" , 'rows' : "3"}),                       
        }

    