from django import forms
from .models import EmployerOrganization, JobPosting

class EmployerOrganizationForm(forms.ModelForm):
    class Meta:
        model = EmployerOrganization
        fields = ['employer_org_name', 'employer_org_description_box', 'representative_claim_token']
        

class JobPostingForm(forms.ModelForm):
    class Meta:
        model = JobPosting
        fields = ['title', 'role_overview', 'role_requirements_and_preferences', 'action_steps',]
        