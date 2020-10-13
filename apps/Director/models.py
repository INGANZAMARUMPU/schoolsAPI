from django.db import models
from django.utils.text import slugify
from django.utils import timezone

class Cni(models.Model):
	cni = models.CharField(max_length=100)

	def __str__(self):
		return f"{self.cni}"

class Commune(models.Model):
	name = models.CharField(max_length=100)
	province = models.ForeignKey('Province', on_delete=models.CASCADE)
	slug = models.SlugField(max_length=100, unique=True)
	date = models.DateTimeField ( default = timezone.now )

	def save( self, *args, **kwargs ):
		self.slug = slugify(self.name+str(self.date))
		super( Commune, self ).save( *args, **kwargs )

	def __str__(self):
		return f"{self.name} {self.province}"

	class Meta:
		unique_together = ('name', "province")
		
class Province(models.Model):
	name = models.CharField( max_length=100 )
	slug = models.SlugField( max_length=100 )
	date = models.DateTimeField ( default = timezone.now )

	def save( self, *args, **kwargs ):
		self.slug = slugify(self.name+str(self.date))#to compare if the we found identical values
		super( Province, self ).save( *args, **kwargs )

	def __str__(self):
		return f"{self.name}"

class School(models.Model):
	name = models.CharField(max_length=1000)
	added_by = models.ForeignKey(User, on_delete=models.CASCADE)
	province = models.ForeignKey('Director.Province', null=True, on_delete=models.SET_NULL)
	commune = models.ForeignKey('Director.Commune', null=True, on_delete=models.SET_NULL)
	zone = models.ForeignKey('Director.Zone', verbose_name='quarter', null=True, on_delete=models.SET_NULL)
	school_type = models.ForeignKey('Director.SchoolType', null=True, on_delete=models.SET_NULL)
	description = models.TextField(max_length=1000)
	visible = models.BooleanField(default=False)
	slug = models.SlugField(max_length=100, unique=True, null=True)
	date = models.DateTimeField ( default = timezone.now )


	def __str__(self):
		return f"{self.name} - {self.zone}"

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name+str(self.date))
		super(School, self).save(*args, **kwargs)

	class Meta:
		unique_together = ('name', 'zone')

class SchoolType(models.Model):
	education = models.CharField(max_length=20)

	def __str__(self):
		return f"{self.education}"

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
