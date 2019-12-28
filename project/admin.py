from django.contrib import admin
from .models import Enq, Addmission, Batch

# Register your models here.

admin .site.register(Enq)
admin .site.register(Addmission)
admin .site.register(Batch)