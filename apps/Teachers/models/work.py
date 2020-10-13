from django.db import models
from django.utils import timezone

class Work(models.Model):
	course = models.ForeignKey("Prefect.Course", null=True, on_delete=models.SET_NULL)
	number = models.IntegerField()
	school_year = models.ForeignKey("Base.SchoolYear", null=True, on_delete=models.SET_NULL)
	maxima = models.IntegerField(null=True)
	date = models.DateField(default=timezone.now)
	work_type = models.ForeignKey("WorkType", null=True, on_delete=models.SET_NULL)
	is_valid = models.BooleanField(default=True, blank=True, null=True)
	category = models.ForeignKey("Category", on_delete=models.CASCADE)

	def __str__(self):
		return f"work {self.course.name} #{self.number}"

	class Meta:
		unique_together = ('course', 'number', 'school_year','category')