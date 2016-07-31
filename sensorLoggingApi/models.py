from __future__ import unicode_literals

from django.db import models

# Create your models here.
class EventData(models.Model):
	videoFile = models.BinaryField()
	pub_date = models.DateTimeField('date published')
	
	def __unicode__(self):
		return self.pub_date

class SensorData(models.Model):
	humid = models.FloatField()
	temperature = models.FloatField()
	pub_date = models.DateTimeField('date published')

	def __unicode__(self):
		return "{0}% {1} C".format(humid, temperature)
