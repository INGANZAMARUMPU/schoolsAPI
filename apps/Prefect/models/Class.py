from django.db import models
from .level import Level
from .section import Section

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
