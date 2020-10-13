from django.db import models

class WorkType(models.Model):
	work_type = models.TextField(max_length=100);

	def __str__(self):
		return self.work_type
