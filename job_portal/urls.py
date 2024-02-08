from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='home'),

    #++++++++ auth ++++++++++
    path('registration/', views.registration, name='registration'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    #++++++++++++++++++++++++

    path('admins/', views.admin, name='admins'),
    path('upload_job/', views.upload_job, name='upload_job'),
    path('create_job/', views.create_job, name='create_job'),
    path('jobs_display/', views.display_jobs, name='jobs_display'),
    path('update_job/<str:pk>', views.updateJob, name="update_job"),
    path('delete_job/<str:pk>', views.deleteJob, name="delete_job"),
    re_path(r'^job-details/(?P<pk>[\w-]+)/$', views.job_Details, name="job-details"),
    path('filter/', views.index, name='filter'),
]