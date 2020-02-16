from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.


class Enq(models.Model):
    edate = models.CharField(max_length=100, default=None)
    enqalias = models.CharField(max_length=50, default=None)
    enqid = models.IntegerField(default=0)
    fname = models.CharField(max_length=50, default=None)
    lname = models.CharField(max_length=50, default=None)
    email = models.EmailField(max_length=50, default=None)
    phone = models.IntegerField(default=0)
    Address = models.CharField(max_length=5000)
    courses = models.CharField(max_length=50)
    enquiry = models.CharField(max_length=70, default=None)
    reference_name = models.CharField(max_length=70, default=None,blank=True)
    status = models.CharField(max_length=70, default=None)
    collagename = models.CharField(max_length=100, default=None,blank=True)
    stream = models.CharField(max_length=50, default=None,blank=True)
    year = models.CharField(max_length=50, default=None, blank=True, null=True)
    company = models.CharField(max_length=50, default=None,blank=True)
    designation = models.CharField(max_length=50, default=None,blank=True)
    year_exper = models.CharField(max_length=50, default=None,blank=True)
    Preferred_day =  models.CharField(max_length=50, default=None)
    weekday_date = models.CharField(max_length=50, default=None,blank=True)
    weekdays_time = models.CharField(max_length=50, default=None,blank=True)
    weekend_date = models.CharField(max_length=50, default=None,blank=True)
    weekend_time = models.CharField(max_length=50, default=None,blank=True)
    comments = models.CharField(max_length=50, default=None)


    def __str__(self):
        return self.enqalias   

    def __iter__(self):
        for field_name in self._meta.get_fields():
            last = str(field_name).split('.')[-1]
            value = getattr(self, last, None)
            yield (field_name, value)       
    

class Addmission(models.Model):
    edate = models.CharField(max_length=100, default=None)
    enqalias = models.CharField(max_length=50, default=None)
    enqid = models.IntegerField(default=0)
    fname = models.CharField(max_length=50, default=None)
    lname = models.CharField(max_length=50, default=None)
    email = models.CharField(max_length=50, default=None)
    phone = models.IntegerField(default=0)
    Address = models.CharField(max_length=5000)
    courses = models.CharField(max_length=50, default=None)
    tot_fees =  models.CharField(max_length=50)
    one_install_date = models.CharField(max_length=50)
    one_install_fees = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    two_install_date1 = models.CharField(max_length=50)
    two_install_fees1 = models.CharField(max_length=50)
    two_install_date2 = models.CharField(max_length=50)
    two_install_fees2 = models.CharField(max_length=50)
    three_install_date1 = models.CharField(max_length=50)
    three_install_fees1 = models.CharField(max_length=50)
    three_install_date2 = models.CharField(max_length=50)
    three_install_fees2 = models.CharField(max_length=50)
    three_install_date3 = models.CharField(max_length=50)
    three_install_fees3 = models.CharField(max_length=50)
    status1 = models.CharField(max_length=50)
    status2 = models.CharField(max_length=50)
    status3 = models.CharField(max_length=50)
    comments = models.CharField(max_length=5000)


    def __str__(self):
        return self.fname

    def __iter__(self):
        for field_name in self._meta.get_fields():
            last = str(field_name).split('.')[-1]
            value = getattr(self, last, None)
            yield (field_name, value)       
        

class Batch(models.Model):
    edate = models.CharField(max_length=100, default=None)
    batchid = models.IntegerField(default=0)
    batchalias = models.CharField(max_length=50, default=None)
    trainer = models.CharField(max_length=50)
    courses = models.CharField(max_length=50, default=None)
    batch_time = models.CharField(max_length=50, default=None)
    batch_days = models.CharField(max_length=50, default=None)
    

    def __str__(self):
        return self.batchalias

    def __iter__(self):
        for field_name in self._meta.get_fields():
            last = str(field_name).split('.')[-1]
            value = getattr(self, last, None)
            yield (field_name, value)       
        
