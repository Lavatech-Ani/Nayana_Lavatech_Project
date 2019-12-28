
from django.urls import path
from . import views

urlpatterns = [
    path("enq/", views.enq, name='enq'),
    path("addmission/", views.addmission, name='addmission'),
    path("batch/", views.batch, name='batch'),
]