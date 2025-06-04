from django.contrib import admin
from .models import EmployerOrganization, JobPosting

class EmployerOrganizationAdmin(admin.ModelAdmin):
    list_display = ('employer_org_name','employer_org_description_box')  
    search_fields = ['employer_org_name']

admin.site.register(EmployerOrganization, EmployerOrganizationAdmin)  



class JobPostingAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'organization', 'post_date', 'expiration_date', 'is_active')
    list_filter = ('organization', 'post_date', 'is_active')
    search_fields = ('title', 'organization__name')  

admin.site.register(JobPosting, JobPostingAdmin)
