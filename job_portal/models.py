from django.db import models
import uuid
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError

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

class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    username = models.CharField(max_length=100, null=False)
    email = models.CharField(max_length=100, null=False, unique=True)
    password = models.CharField(max_length=100, null=False)
    confirm_password = models.CharField(max_length=100, null=False)
    role = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # Hash the password and confirm_password before saving
        self.password = make_password(self.password)
        self.confirm_password = make_password(self.confirm_password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username

