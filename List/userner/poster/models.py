from django.db import models
from django.conf import settings
# Create your models here.
User = settings.AUTH_USER_MODEL

class Snippet(models.Model):
	user = models.ForeignKey(User, default=1,null=True,on_delete=models.CASCADE)
	blogname = models.CharField(max_length=100)
	blogauth = models.CharField(max_length=100)
	blogdes = models.TextField(max_length=400)
	img = models.ImageField(upload_to='static', null=True)
	
	def __str__(self):
		return self.blogname

	def get_absolute_url(self):
		return f'/profile/{self.user.username}/{self.id}'