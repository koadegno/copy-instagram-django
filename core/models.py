from distutils.command.upload import upload
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model() 

class Profile(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	id_user = models.IntegerField()
	bio = models.TextField(blank=True)
	phone = models.IntegerField(blank=True)
	profile_image = models.ImageField(upload_to='profile_image', default='default_profile_picture.png')

	def __str__(self) -> str:
		profile = f"\n{self.user} ({self.user_id}) \n{self.phone}\n{self.bio}"
		return super().__str__()+profile