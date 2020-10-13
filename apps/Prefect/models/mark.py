from django.db import models

class Mark(models.Model):
	student = models.ForeignKey('Student', related_name='who', on_delete=models.CASCADE)
	course = models.ForeignKey('Course', on_delete=models.CASCADE)
	work_first_term = models.IntegerField(null=True, blank=True)
	exam_first_term = models.IntegerField(null=True, blank=True)
	work_second_term = models.IntegerField(null=True, blank=True)
	exam_second_term = models.IntegerField(null=True, blank=True)
	work_third_term = models.IntegerField(null=True, blank=True)
	exam_third_term = models.IntegerField(null=True, blank=True)

	def __str__(self):
		return f"{self.student} {self.course}"
