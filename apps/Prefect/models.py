from django.db import models

class Class(models.Model):
	section = models.ForeignKey('Section', on_delete=models.CASCADE)
	school = models.ForeignKey('Director.School', on_delete=models.CASCADE)
	level = models.ForeignKey('Level', on_delete=models.CASCADE, verbose_name='Level')
	titulaire = models.ForeignKey('Base.Profil', null=True, on_delete=models.SET_NULL)
	group = models.CharField(max_length=100, blank=True, null=True)

	def __str__(self):
		return f"{self.level} {self.section} {self.school}"

	class Meta:
		unique_together = ('section', 'school', 'level', 'group')
		verbose_name_plural = 'Classes'

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

class Level(models.Model):
	name = models.CharField(max_length=100, unique=True)

	def __str__(self):
		return self.name

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

class Section(models.Model):
	name = models.CharField(max_length=100, unique=True)

	def __str__(self):
		return self.name

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

class StudentWork(models.Model):
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

	class Meta:
		unique_together = ('student','course',)

