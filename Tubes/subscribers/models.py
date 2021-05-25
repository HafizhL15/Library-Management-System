from django.db import models

# Create your models here.

class Pelanggan(models.Model):
	tipe	  	= models.CharField(max_length=100)
	name 		= models.CharField(max_length=100)
	address		= models.CharField(max_length=100)
	phone		= models.CharField(max_length=100)
	email		= models.EmailField(max_length=100)

	def __str__(self):
		return "{}.{}".format(self.id,self.name)