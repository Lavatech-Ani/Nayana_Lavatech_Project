
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name="project"),
    path("enq/", views.enq, name='enq'),
    path("addmission/", views.addmission, name='addmission'),
    path("batch/", views.batch, name='batch'),
    path("alias/", views.alias, name='alias'),
]