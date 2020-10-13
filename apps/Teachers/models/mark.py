from django.db import models
from .work import Work

class Mark(models.Model):
	student = models.ForeignKey('Prefect.Student', on_delete=models.CASCADE)
	work = models.ForeignKey('Work', on_delete=models.CASCADE)
	marks = models.IntegerField(null=True, blank=True)

	def __str__(self):
		return f"{self.student} in {self.work} : {self.marks}"

	class Meta:
		unique_together = ('student', 'work', 'marks')