
from django.urls import path, include
from . import views


urlpatterns = [
    path("",views.index, name="project"),
    path("enq/", views.enq, name='enq'),
    path("enq1/", views.enq1, name='enq1'),
    path("addmission/", views.addmission, name='addmission'),
    path("batch/", views.batch, name='batch'),
    path("createalias/", views.createalias, name='createalias'),
    path("studentdata/", views.studentdata, name='studentdata'),
    path("searchenq/", views.searchenq, name='searchenq'),
    path("searchaddmission/", views.searchaddmission, name='searchaddmission'),
    path("searchbatch/", views.searchbatch, name='searchbatch'),
    path("modifyenq/", views.modifyenq, name='modifyenq'),
    path("modifyaddmission/", views.modifyaddmission, name='modifyaddmission'),
    path("modifybatch/", views.modifybatch, name='modifybatch'),
    path("reportenq/", views.reportenq, name='reportenq'),
    path("reportbatch/", views.reportbatch, name='reportbatch'),
    path("reportcontact/", views.reportcontact, name='reportcontact'),
    path("feesnew/", views.feesnew, name='feesnew'),
    path("feesreport/", views.feesreport, name='feesreport'),
    path("feessearch/", views.feessearch, name='feessearch'),
    path("internnew/", views.internnew, name='internnew'),
    path("internupdate/", views.internupdate, name='internupdate'),
    
]