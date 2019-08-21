from django.db import models
from django.contrib.auth.models import User
from PIL import Image




# Create your models here.
class Profile(models.Model):
	user=models.OneToOneField(User, on_delete=models.CASCADE) 
	#make one to one relationship to the user model 
	#in the ondelete specificied the user profile is automatically deleted if the user is deleted
	image=models.ImageField(default='default.jpg', upload_to='profile_pics')
	#other fields can be added here after images, such as city e.t.c

	def __str__(self):
		return f'{self.user.username} Profile'
	#to prevent it from printing out jubrish, i use the dunder str function

	#remember whenever we make a change, it changes the database, therefore it is necessary to
	#to make the migrations, we make use of the migration to trey to make the migrations
	#later: pillow is installed so that i can make use of images 
	
	def save(self):
	# this method already exist in our parent class and its gloing
	#to be overriden with this, the essense is to use this to try to reduce the image size using pillow
		super().save()
		#open image of the current instance
		img=Image.open(self.image.path)

		if img.height > 300 or img.width > 300:
			output_size=(300, 300)
			img.thumbnail(output_size)
			img.save(self.image.path)

