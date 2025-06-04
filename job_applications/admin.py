from django.contrib import admin
from .models import JobApplication

class JobApplicationsAdmin(admin.ModelAdmin):

    def get_job_posting_title(self, obj):
        # Этот метод вернет название публикации о вакансии.
        return obj.job_posting.title
    get_job_posting_title.short_description = 'Job Title'

    def get_employer_organization_name(self, obj):
        # Этот метод вернет название организации работодателя, связанное с размещением вакансии.
        return obj.job_posting.organization.employer_org_name
    get_employer_organization_name.short_description = 'Employer Organization'

    def get_job_posting_id(self, obj):
        # Этот метод вернет идентификатор публикации вакансии.
        return obj.job_posting.id
    get_job_posting_id.short_description = 'Job Posting ID'

    def get_employer_organization_id(self, obj):
        # Этот метод вернет идентификатор организации-работодателя, связанной с размещением вакансии.
        return obj.job_posting.organization.id
    get_employer_organization_id.short_description = 'Employer Org ID'

    list_display = (
        'id',

        'get_employer_organization_name',
        'get_employer_organization_id',

        'get_job_posting_title',
        'get_job_posting_id',

        'user',
        'submit_date',
        'linkedin_url'
    )
    search_fields = (
        'user__username',
        'job_posting__title',
        'job_posting__organization__employer_org_name'
    )

admin.site.register(JobApplication, JobApplicationsAdmin)
