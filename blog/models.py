#models.py are related to database

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User #User is django built-in user
from django.urls import reverse

class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	#get_absolute_url method is a way to tell django to find the url of model object like here of post-detail url
	def get_absolute_url(self): 
		#reverse will return full path as string to url or urls.py and kwargs is for extra parameter for that DetailView
		return reverse('post-detail', kwargs={'pk':self.pk}) 


class About_descript(models.Model):
	content = models.TextField()

	def __str__(self):
		return self.content
