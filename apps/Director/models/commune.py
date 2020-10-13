from django.db import models
from .province import Province
from django.utils.text import slugify
from django.utils import timezone

class Commune(models.Model):
	name = models.CharField(max_length=100)
	province = models.ForeignKey('Province', on_delete=models.CASCADE)
	slug = models.SlugField(max_length=100, unique=True)
	date = models.DateTimeField ( default = timezone.now )

	def save( self, *args, **kwargs ):
		self.slug = slugify(self.name+str(self.date))#to compare if the we found identical values
		super( Commune, self ).save( *args, **kwargs )

	def __str__(self):
		return f"{self.name} {self.province}"

	class Meta:
		unique_together = ('name', "province")
