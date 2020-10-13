from django.db import models
from django.utils import timezone

class Appel(models.Model):
	course = models.ForeignKey('Prefect.Course', on_delete=models.CASCADE)
	date = models.DateField(default=timezone.now)

	def __str__(self):
		return f"{self.course} on {self.date}"