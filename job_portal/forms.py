from django.forms import ModelForm
from .models import *

class JobForm(ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'company', 'location', 'salary', 'job_type', 'Job_Description', 'link']