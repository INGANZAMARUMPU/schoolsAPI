from django.db import models
from .appel import Appel

class Presence(models.Model):
	appel = models.ForeignKey('Appel', on_delete=models.CASCADE)
	student = models.ForeignKey('Prefect.Student', on_delete=models.CASCADE)
	is_present = models.BooleanField(null=True)

	def __str__(self):
		present = "present" if self.is_present else "absent"
		return f"{self.student} on {present}"