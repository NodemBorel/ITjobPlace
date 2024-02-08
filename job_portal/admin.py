from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Job, User

# Register your models here.

admin.site.register(Job)
admin.site.register(User)

class JobImport(ImportExportModelAdmin):
    list_display = ('title', 'company', 'location', 'salary', 'job_type', 'Job_Description', 'link')