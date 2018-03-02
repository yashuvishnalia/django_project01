from django.db import models
# from django.utils import timezone
from django.urls import reverse

import random
import os
def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext
def upload_image_path(instance, filename):
    # print(instance)
    #print(filename)
    new_filename = random.randint(1,3910209312)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "products/{new_filename}/{final_filename}".format(
            new_filename=new_filename,
            final_filename=final_filename
)

class Album(models.Model):
	artist = models.CharField(max_length=250)
	album_title= models.CharField(max_length=500)
	album_logo= models.ImageField(upload_to=upload_image_path,null=True,blank=True)
	# or
	# album_logo= model.FileField()

	# add_date = models.DateTimeField('date published')

	def get_absolute_url(self):
		return reverse('music:detail', kwargs={'pk':self.pk})

	def __str__(self):
		return self.artist + '-' + self.album_logo

	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Song(models.Model):
	album = models.ForeignKey(Album, on_delete=models.CASCADE)
	title = models.CharField(max_length=500)
	is_favourite = models.BooleanField(default=False)

	def __str__(self):
		return self.title
