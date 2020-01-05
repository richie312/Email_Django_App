from django.db import models

# Create your models here.
class BlogPost(models.Model):
	title = models.TextField()
	content = models.CharField(max_length = 100, null = True,blank = True) 
	