from django.shortcuts import render, get_object_or_404, redirect

from django.contrib import messages

from .forms import EmployerOrganizationForm, JobPostingForm

from django.http import HttpResponse

from .models import EmployerOrganization, JobPosting 
from core.models import UserProfile
from job_applications.models import JobApplication  

from django.urls import reverse
from django.utils import timezone


def index(request):
    return HttpResponse("Job Catalog app section")

def display_all_companies(request):  
    all_organizations = EmployerOrganization.objects.all()
    context = {'organizations_list': all_organizations}  
    return render(request, 'job_catalog/all_companies.html' ,context)  



def display_all_jobs(request):
    all_jobs = JobPosting.objects.all()
    context = {'job_postings_list': all_jobs} 
    return render(request, 'job_catalog/all_jobs.html' ,context)


def job_details(request, job_id):
    job_instance = get_object_or_404(JobPosting, pk=job_id)
    user_has_applied = False
    application = None

    if request.user.is_authenticated:
        try:
            application = JobApplication.objects.get(job_posting=job_instance, user=request.user)
            user_has_applied = True
        except JobApplication.DoesNotExist:
            user_has_applied = False

    context = {
        'job_instance': job_instance,
        'user_has_applied': user_has_applied,
        'application': application,  
    }
    return render(request, 'job_catalog/job_details.html', context)

def company_details(request, company_id):
    company_instance = get_object_or_404(EmployerOrganization, pk=company_id)
    total_job_postings = JobPosting.objects.filter(organization=company_instance).count()
    active_job_postings = JobPosting.objects.filter(organization=company_instance, is_active=True).count()
    job_postings = JobPosting.objects.filter(organization=company_instance, is_active=True)

    context = {
        'company_instance': company_instance,
        'job_postings': job_postings,
        'total_job_postings': total_job_postings,  
        'active_job_postings': active_job_postings,  
    }
    return render(request, 'job_catalog/company_details.html', context)


def create_organization(request):
    if not request.user.is_authenticated:
        messages.error(request, "You must be logged in to create an organization.")
        return redirect('core:login_start')

    user_profile = UserProfile.objects.get(user=request.user)
    if user_profile.organization:
        org_name = user_profile.organization.employer_org_name
        messages.error(request,
                       f"You cannot create a company since you are currently representing {org_name} for hiring.")
        return redirect('job_catalog:index')

    if request.method == 'POST':
        form = EmployerOrganizationForm(request.POST)
        if form.is_valid():
            new_organization = form.save()
            user_profile.organization = new_organization
            user_profile.save()
            messages.success(request, "Organization created successfully.")
            return redirect('job_catalog:index') 
    else:
        form = EmployerOrganizationForm()

    return render(request, 'job_catalog/create_organization_form.html', {'form': form})

def create_job_posting(request):
    print("Entered create_job_posting view")
    if not request.user.is_authenticated:
        messages.error(request, "You must be logged in to post a job.")
        return redirect('core:login_start')

    if not hasattr(request.user, 'profile') or not request.user.profile.organization:
        messages.error(request, "You need to be associated with an organization to post a job.")
        return redirect('/')  

    if request.method == 'POST':
        form = JobPostingForm(request.POST)
        print("Form created")
        if form.is_valid():
            print("Form is valid")
            job_posting = form.save(commit=False)
            job_posting.organization = request.user.profile.organization 
            job_posting.post_date = timezone.now()
            job_posting.expiration_date = timezone.now() + timezone.timedelta(days=90)
            job_posting.save()
            print(f"Job Posting created with ID: {job_posting.id}")
            messages.success(request, 'Job posting created successfully.')
            return redirect(reverse('job_catalog:job_details', args=[job_posting.id]))
        else:
            print("Form is not valid")
            print(form.errors)
    else:
        form = JobPostingForm()

    return render(request, 'job_catalog/create_job_posting.html', {'form': form})