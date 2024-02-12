from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import *

class StaticSitemap(Sitemap):
    def items(self):
        return ['home', 'login', 'registration']
    
    #takes each individual item form th item function and create an url
    def location(self, item):
        return reverse(item)

class JobSitemap(Sitemap):
    def items(self):
        return Job.objects.all()[:100]  

    def lastmod(self, obj):
        return obj.updated_at 
    
