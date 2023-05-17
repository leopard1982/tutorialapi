from django.db import models

# Create your models here.
class books(models.Model):
	judul = models.CharField(max_length=200,null=False,primary_key=True,blank=True)
	pengarang = models.CharField(max_length=200,null=True,blank=True)
	isbn = models.CharField(max_length=200,null=True,blank=True)
	
	def __str__(self):
		return self.judul