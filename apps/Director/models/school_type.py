from django.db import models

class SchoolType(models.Model):
	education = models.CharField(max_length=20)

	def __str__(self):
		return f"{self.education}"
