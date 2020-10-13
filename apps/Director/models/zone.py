from django.db import models
from .commune import Commune
from django.utils.text import slugify
from django.utils import timezone

class Zone(models.Model):
	name = models.CharField(max_length=100)
	commune = models.ForeignKey('Commune', on_delete=models.CASCADE)
	slug = models.SlugField(max_length=100)
	date = models.DateTimeField ( default = timezone.now )

	def save( self, *args, **kwargs ):
		self.slug = slugify(self.name+str(self.date))#to compare if the we found identical values
		super( Zone, self ).save( *args, **kwargs )

	def __str__(self):
		return f"{self.name}"

	class Meta:
		unique_together = ('name', 'commune')
