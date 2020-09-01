from django.db import models

# Create your models here.
class City(models.Model):
	name = models.CharField(max_length = 25)
	cityid = models.IntegerField(blank = True, null = True)
	description = models.CharField(max_length = 250,blank = True, null = True )
	ftemp = models.FloatField(blank = True, null = True)
	ctemp = models.FloatField(blank = True, null = True)
	flag = models.IntegerField(default = 0)
	icon = models.CharField(max_length=50,blank = True, null = True)
	
	def __str__(self):
		return self.name