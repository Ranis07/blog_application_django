from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE) #on_delete means if the user is deleted then its profile will also get automatically deleted.
	image = models.ImageField(default='defaults.jpg', upload_to='profile_pics') #default is profile uses that image as a default and upload_to means the user selected pic for his profile will be stored there.

	def __str__(self):
		return f'{self.user.username} Profile'

	def save(self, *args,**kwargs): #this method is for saving the uploaded pic by reducing its size
		super().save(*args,**kwargs) #it is the parent class save() method
		img = Image.open(self.image.path) #Image is imported from Pillow
		if img.height >300 or img.width >300:
			output_size = (300,300)
			img.thumbnail(output_size) #thumbnail makes the img size according to output_size
			img.save(self.image.path) #saving in the same path

