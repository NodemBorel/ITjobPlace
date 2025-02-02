from django.db import models
import uuid

# Create your models here.
class Job(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField(max_length=1000000, null=False)
    company = models.CharField(max_length=10000000, null=True)
    location = models.CharField(max_length=10000000, null=True)
    salary = models.CharField(max_length=10000000, null=True)
    job_type = models.CharField(max_length=10000000, null=True)
    Job_Description = models.CharField(max_length=10000000, null=False)
    link = models.CharField(max_length=10000000, null=False)
    on_click = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/job_details/{self.id}'

