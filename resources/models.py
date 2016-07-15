from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse

# Create your models here.

class Driver(models.Model):
	name= models.CharField(max_length=128)

class Manufacture(models.Model):
	name = models.CharField(max_length=30, unique=True)
	def __str__(self):
		return self.name

class Vehicle(models.Model):

 	name = models.CharField(max_length=30)
 	description= models.TextField(null=True)
 	license_plate= models.CharField(max_length=7)
 	manufacture_year= models.DateField()
 	is_active= models.BooleanField(default=True)
 	usecontrols= models.ManyToManyField(Driver, through='UseControl')
 	manufaturer= models.ForeignKey(Manufacture, on_delete=models.CASCADE)

 	def get_absolute_url(self):
 		return reverse('vehicle_create')


class UseControl(models.Model):
	driver = models.ForeignKey(Driver)
	vehicle= models.ForeignKey(Vehicle)
	date_started= models.DateTimeField(auto_now_add=True)
	date_ended= models.DateTimeField(blank=True, null=True)

class Manager(models.Model):
	user= models.OneToOneField(settings.AUTH_USER_MODEL, primary_key=True)
	name= models.CharField(max_length=30)


