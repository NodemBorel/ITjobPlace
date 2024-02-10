from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Job

# Register your models here.

admin.site.register(Job)

class JobImport(ImportExportModelAdmin):
    list_display = ('title', 'company', 'location', 'salary', 'job_type', 'Job_Description', 'link')