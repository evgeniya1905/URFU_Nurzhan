from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import home_view, RegisterUserView, LoginStartView, ClaimOrganizationView, before_leaving_organization, leave_organization_confirmed


app_name = 'core'  

urlpatterns = [
    path('', home_view, name='home'),  
    path('register_user/', RegisterUserView.as_view(), name = 'register'),  
    path('login_start/', LoginStartView.as_view(), name = 'login_start'),
    path('logout/', LogoutView.as_view(), name = 'logout'), 

    path('claim_org/', ClaimOrganizationView.as_view(), name='claim_organization'),
    path('leave_org/', before_leaving_organization, name='leaving_organization'), 
    path('leave_organization/confirm/', leave_organization_confirmed, name='left_organization_confirmation'),

]