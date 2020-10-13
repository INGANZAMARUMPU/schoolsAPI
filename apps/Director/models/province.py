from django.db import models
from django.utils.text import slugify
from django.utils import timezone

class Province(models.Model):
	name = models.CharField( max_length=100 )
	slug = models.SlugField( max_length=100 )
	date = models.DateTimeField ( default = timezone.now )

	def save( self, *args, **kwargs ):
		self.slug = slugify(self.name+str(self.date))#to compare if the we found identical values
		super( Province, self ).save( *args, **kwargs )

	def __str__(self):
		return f"{self.name}"
