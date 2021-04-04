from django.db import models

# Create your models here.
class ExoplanetsData(models.Model):
	host_name = models.CharField(max_length=200)
	discovery_year = models.IntegerField()
	discovery_method = models.CharField(max_length=100)
	light_years = models.IntegerField()
	planet_mass = models.FloatField()
	discovery_facility = models.CharField(max_length=100)

	def __str__(self):
		return self.host_name