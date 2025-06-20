from django.urls import path
from . import views

app_name = 'job_catalog'

urlpatterns = [
    path('', views.index, name='index'),
    path('all_companies/', views.display_all_companies, name='all_companies'),
    path('all_jobs/', views.display_all_jobs, name='all_jobs'),

    path('job/<int:job_id>/', views.job_details, name='job_details'),
    path('company/<int:company_id>/', views.company_details, name='company_details'),

    path('new_org/', views.create_organization, name='create_organization'),

    path('create_job/', views.create_job_posting, name='create_job_posting'),
]
