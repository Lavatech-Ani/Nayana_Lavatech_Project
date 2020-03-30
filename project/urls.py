
from django.urls import path, include
from . import views


urlpatterns = [
    path("",views.index, name="project"),
    path("enq/", views.enq, name='enq'),
    path("StudentAlias/", views.StudentAlias, name='StudentAlias'),
    path("addmission/", views.addmission, name='addmission'),
    path("batch/", views.batch, name='batch'),
    path("searchenq/", views.searchenq, name='searchenq'),
    path("searchaddmission/", views.searchaddmission, name='searchaddmission'),
    path("searchbatch/", views.searchbatch, name='searchbatch'),
    path("Serach_Enq_Alias/", views.Serach_Enq_Alias, name='Serach_Enq_Alias'),
    path("modifyenq/", views.modifyenq, name='modifyenq'),
    path("Serach_Addmission_Alias/", views.Serach_Addmission_Alias, name='Serach_Addmission_Alias'),
    path("modifyaddmission/", views.modifyaddmission, name='modifyaddmission'),
    path("Serach_Batch_Alias/", views.Serach_Batch_Alias, name='Serach_Batch_Alias'),
    path("modifybatch/", views.modifybatch, name='modifybatch'),
    path("reportenq/", views.reportenq, name='reportenq'),
    path("reportbatch/", views.reportbatch, name='reportbatch'),
    path("reportcontact/", views.reportcontact, name='reportcontact'),
    path("feesnewserach/", views.feesnewserach, name='feesnewserach'),
    path("feesnew/", views.feesnew, name='feesnew'),
    path("feesreport/", views.feesreport, name='feesreport'),
    path("feessearch/", views.feessearch, name='feessearch'),
    path("internnew/", views.internnew, name='internnew'),
    path("internupdate/", views.internupdate, name='internupdate'),
    
]