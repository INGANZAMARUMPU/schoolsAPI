from django.db import models
from django.utils import timezone

class Appel(models.Model):
	course = models.ForeignKey('Prefect.Course', on_delete=models.CASCADE)
	date = models.DateField(default=timezone.now)

	def __str__(self):
		return f"{self.course} on {self.date}"

class Category(models.Model):
	category = models.TextField(max_length=100)

	def __str__(self):
		return self.category

class Mark(models.Model):
	student = models.ForeignKey('Prefect.Student', on_delete=models.CASCADE)
	work = models.ForeignKey('Work', on_delete=models.CASCADE)
	marks = models.IntegerField(null=True, blank=True)

	def __str__(self):
		return f"{self.student} in {self.work} : {self.marks}"

	class Meta:
		unique_together = ('student', 'work', 'marks')

class Presence(models.Model):
	appel = models.ForeignKey('Appel', on_delete=models.CASCADE)
	student = models.ForeignKey('Prefect.Student', on_delete=models.CASCADE)
	is_present = models.BooleanField(null=True)

	def __str__(self):
		present = "present" if self.is_present else "absent"
		return f"{self.student} on {present}"

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

class WorkType(models.Model):
	work_type = models.TextField(max_length=100);

	def __str__(self):
		return self.work_type