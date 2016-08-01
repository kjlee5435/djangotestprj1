from __future__ import unicode_literals

from django.db import models

# Create your models here.
class EventData(models.Model):
	pub_date = models.DateTimeField('date published')
	fileName = models.CharField(max_length=200, default="")
	
	def __unicode__(self):
		return "{0} : {1}".format(self.pub_date, self.fileName)

class SensorData(models.Model):
	humid = models.FloatField()
	temperature = models.FloatField()
	pub_date = models.DateTimeField('date published')

	def __unicode__(self):
		return "{0} : {1}% {2} C".format(self.pub_date, self.humid, self.temperature)
