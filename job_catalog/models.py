from django.db import models
from django.utils import timezone  


class EmployerOrganization(models.Model):
    employer_org_name = models.CharField(max_length = 50)
    employer_org_description_box = models.TextField(
        default = 'Describe your organization, but not a specific role or requirements',
        blank = False  
        )
    representative_claim_token = models.CharField(max_length = 16, default = "join")
    def __str__(self):
        return self.employer_org_name


class JobPosting(models.Model):
    organization = models.ForeignKey(EmployerOrganization, on_delete=models.CASCADE, default = 1)  
    title = models.CharField(max_length=100)
    role_overview = models.TextField()
    role_requirements_and_preferences = models.TextField()
    action_steps = models.TextField()
    post_date = models.DateTimeField(auto_now=True)
    expiration_date = models.DateTimeField(default=timezone.now() + timezone.timedelta(days=90))
    is_active = models.BooleanField(default=True)

    
    def save(self, *args, **kwargs):
        if self.expiration_date < timezone.now():
            self.is_active = False
        super().save(*args, **kwargs)