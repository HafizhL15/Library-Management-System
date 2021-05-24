from django.db import models

# Create your models here.

class Peminjam(models.Model):
	subs_id	  		= models.IntegerField(max_length=3)
	borrow_date 	= models.CharField(max_length=100)
	item_id			= models.IntegerField(max_length=3)
	return_date		= models.CharField(max_length=100)
	fee				= models.IntegerField(max_length=10)

	def __str__(self):
		return "{}.{}".format(self.id,self.subs_id)