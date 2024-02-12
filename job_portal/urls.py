from django.urls import path, re_path

from django.contrib.sitemaps.views import sitemap
from django.views.generic.base import TemplateView
from .sitemaps import *
from . import views

sitemaps = {
    'static' : StaticSitemap,
    'jobs' : JobSitemap
}

urlpatterns = [
    path('', views.index, name='home'),

    path('sitemap.xml', sitemap, {'sitemaps':sitemaps}, name="django.contrib.sitemaps.views.sitemap"),
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    
    #++++++++ auth ++++++++++
    path('registration/', views.registration, name='registration'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    #++++++++++++++++++++++++

    path('admins/', views.admin, name='admins'),
    path('upload_job/', views.upload_job, name='upload_job'),
    path('create_job/', views.create_job, name='create_job'),
    path('jobs_display/', views.display_jobs, name='jobs_display'),
    path('update_job/<str:pk>', views.updateJob, name="update_job"),
    path('delete_job/<str:pk>', views.deleteJob, name="delete_job"),
    
    #-----------------job details for comers
    path('job_details/<str:pk>', views.jobDetails, name="job_details"),

    re_path(r'^job-details/(?P<pk>[\w-]+)/$', views.job_Details, name="job-details"),
    path('filter/', views.index, name='filter'),
]