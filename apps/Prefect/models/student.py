from django.db import models
from django.utils import timezone

class Student(models.Model):
	complete_identity = models.ForeignKey('Base.Profil', blank=True,null=True, on_delete=models.SET_NULL)
	firstname = models.CharField(max_length=32)
	lastname = models.CharField(max_length=32)
	Class = models.ForeignKey('Prefect.Class', on_delete=models.CASCADE)
	admission_date = models.DateField(blank=True, default=timezone.now)


	def __str__(self):
		return f"{self.firstname} {self.lastname}"
	class Meta:
		unique_together = ('complete_identity', 'Class')