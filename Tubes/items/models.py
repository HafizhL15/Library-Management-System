from django.db import models

# Create your models here.

class Barang(models.Model):
	librari	  		= models.CharField(max_length=100)
	category 		= models.CharField(max_length=100)
	title			= models.CharField(max_length=100)
	author			= models.CharField(max_length=100)
	publisher		= models.CharField(max_length=100)
	year			= models.IntegerField(max_length=5)
	copies			= models.IntegerField(max_length=10)

	def __str__(self):
		return "{}.{}".format(self.id,self.librari)