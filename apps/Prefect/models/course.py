from django.db import models
from .Class import Class
from django.utils.text import slugify
from apps.Base.models import SchoolYear

class Course(models.Model):
	name = models.CharField(max_length=100)
	Class = models.ForeignKey('Class', on_delete=models.CASCADE)
	prof = models.ForeignKey('Base.Profil', on_delete=models.CASCADE)
	max_ponderation = models.IntegerField()
	duration = models.IntegerField()
	slug = models.SlugField(null=True, max_length=100)
	school_year = models.ForeignKey('Base.SchoolYear', null=True, on_delete=models.SET_NULL)

	def __str__(self):
		return f"{self.name} {self.Class}"

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name+" "+str(self.Class))
		super(Course, self).save(*args, **kwargs)

	class Meta:
		unique_together = ('name', 'Class', 'school_year')
