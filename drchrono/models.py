from django.db import models

# Create your models here.

class Doctor(models.Model):

	username = models.CharField(max_length=100)
	access_token = models.CharField(max_length=100)
	refresh_token = models.CharField(max_length=100)

	def __str__(self):
		return self.username