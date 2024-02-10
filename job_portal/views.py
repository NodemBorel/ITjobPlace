from django.shortcuts import render, redirect
from django.http import JsonResponse
from datetime import datetime, timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *
from .resources import JobResource
from django.contrib import messages
from tablib import Dataset
from django.db.models import Q
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .decorators import unauthenticated_user, admin_only

from .forms import JobForm, RegistrationForm

# Create your views here.

def format_timedelta(td):
    seconds_in_minute = 60
    seconds_in_hour = 3600
    seconds_in_day = 86400

    days, seconds = td.days, td.seconds
    hours, remainder = divmod(seconds, seconds_in_hour)
    minutes, seconds = divmod(remainder, seconds_in_minute)

    if days > 0:
        return f"{days} days"
    elif hours > 0:
        return f"{hours} hours"
    elif minutes > 0:
        return f"{minutes} minutes"
    else:
        return f"{seconds} seconds"


def index(request):
    searchQuery = request.GET.get('q')  # Get the search query from the URL parameters
    #sortOption = request.GET.get('sortOption', '0')
    jobs = Job.objects.all()

    current_time = datetime.now(timezone.utc)
    
    # Loop through each job to calculate time difference
    for job in jobs:
        time_difference = current_time - job.created_at
        formatted_time_difference = format_timedelta(time_difference)
        job.created_at = formatted_time_difference

    objects_per_page = 8

    #if searchQuery:
        # If there is a search query, filter jobs based on title or company containing the query
        #jobs = jobs.filter(Q(title__icontains=searchQuery) | Q(company__icontains=searchQuery))

    paginator = Paginator(jobs, objects_per_page)

    page = request.GET.get('page')
    try:
        objects = paginator.page(page)
    except PageNotAnInteger:
        # If the page is not an integer, deliver the first page.
        objects = paginator.page(1)
    except EmptyPage:
        # If the page is out of range, deliver the last page of results.
        objects = paginator.page(paginator.num_pages)   

    if searchQuery:
        # If there is a search query, filter jobs based on title or company containing the query
        objects = jobs.filter(Q(title__icontains=searchQuery) | Q(company__icontains=searchQuery))    
        for job in objects:
            time_difference = current_time - job.created_at
            formatted_time_difference = format_timedelta(time_difference)
            job.created_at = formatted_time_difference    

    '''if sortOption == '1':
        objects = jobs.order_by('-created_at')  # Newest Post
    elif sortOption == '2':
        objects = jobs.order_by('created_at')  # Oldest Post'''

    context = {'objects':objects}

    return render(request, 'index.html', context)

def job_Details(request, pk):
    job_d = Job.objects.get(id=pk)
    
    # Get the current time
    current_time = datetime.now(timezone.utc)
    
    # Calculate the time difference
    time_difference = current_time - job_d.created_at
    
    formatted_time_difference = format_timedelta(time_difference)

    job_details = {
        'title': job_d.title,
        'company': job_d.company,
        'location': job_d.location,
        'salary': job_d.salary,
        'job_type': job_d.job_type,
        'Job_Description': job_d.Job_Description,
        'link': job_d.link,
        'on_click': job_d.on_click,
        'formatted_time_difference': formatted_time_difference,
    }
    
    return JsonResponse(job_details)

#=========================================== registration / login =====================================
@unauthenticated_user
def registration(request):
    form = RegistrationForm()

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False) 
            user.save()

            group = Group.objects.get(name='user')
            user.groups.add(group)

            if user is not None:
                login(request, user)
                return redirect('login')

    context = {'form': form,}
    return render(request, 'auth/login_registration.html', context)

@unauthenticated_user
def loginUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        
        if username and password:
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Email and password are required.')        
    return render(request, 'auth/login_registration.html')

@login_required
def logoutUser(request):
    logout(request)
    return redirect('home')
#======================================================================================================

@login_required
@admin_only
def admin(request):
    form = JobForm()
    return render(request, 'admin/dashboard.html', {'form':form})

@login_required
@admin_only
def upload_job(request):
    if request.method == 'POST':
        job_resource = JobResource
        dataset = Dataset()
        new_job = request.FILES['myfile']

        if not new_job.name.endswith('xlsx'):
            messages.info(request, 'wrong format')
            return render(request, 'admin/dashboard.html')
        imported_data = dataset.load(new_job.read(), format='xlsx')
        for data in imported_data:
            value = Job(
                data[0],
                data[1],
                data[2],
                data[3],
                data[4],
                data[5],
                data[6],
                data[7],
            )
            value.save()
        messages.info(request, 'Imported Successfully')   
    return redirect('/admins')     
    #return render(request, 'admin/dashboard.html')   

@login_required
@admin_only
def create_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Job Created Successfully')
            return redirect('/admins')
    return render(request, 'admin/dashboard.html') 

@login_required
@admin_only
def display_jobs(request):
    jobs = Job.objects.all()
    total_jobs = jobs.count()
    context = {'jobs':jobs, 'total_jobs':total_jobs}
    return render(request, 'admin/job_board.html', context)

@login_required
@admin_only
def updateJob(request, pk):
    job = Job.objects.get(id=pk)
    form = JobForm(instance=job)

    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            messages.info(request, 'Updates Successfully')
            return redirect('/jobs_display')   
    context = {'form':form}
    return render(request, 'admin/update_job.html', context)

@login_required
@admin_only
def deleteJob(request, pk):
    job = Job.objects.get(id=pk)
    if request.method == 'POST':
        job.delete()
        messages.info(request, 'Deleted Successfully')
        return redirect('/jobs_display')
    context = {'job':job}
    return render(request, 'admin/delete.html', context)
