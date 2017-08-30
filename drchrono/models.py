from django.db import models
from datetime import datetime
import pytz

# Create your models here.

class Doctor(models.Model):

	username = models.CharField(max_length=100)
	access_token = models.CharField(max_length=100)
	refresh_token = models.CharField(max_length=100)
	token_expiration = models.DateTimeField(blank=True, null=True)
	avg_wait_time = models.FloatField(default=0.0)
	patients_seen = models.IntegerField(default=0)

	def __str__(self):
		return self.username

class Patient(models.Model):

	pid = models.IntegerField()
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	scheduled_time = models.DateTimeField()
	duration = models.IntegerField()
	checkin_time = models.DateTimeField(blank=True, null=True)
	wait_time = models.FloatField(default=0.0)
	status = models.CharField(max_length=100, blank=True, null=True)

	def __str__(self):
		return self.first_name + " " + self.last_name