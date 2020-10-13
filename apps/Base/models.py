from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Attribution(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	role = models.ForeignKey("Role", on_delete=models.CASCADE)
	school = models.ForeignKey("Director.School", on_delete=models.CASCADE)
	depuis = models.DateField(verbose_name='since',default=timezone.now,blank=True)

	def __str__(self):
		return f"{self.role} at {self.school}"

	class Meta:
		unique_together = ('user', 'role', 'school')

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, unique=True,on_delete=models.CASCADE)
    avatar = models.ImageField(null=True, blank=True, upload_to="avatars/")
    matricule = models.IntegerField(null=True, blank=True, )
    birthday = models.DateField(null=True, blank=True, max_length=100)
    father_name = models.CharField(null=True, blank=True, max_length=100)
    mother_name = models.CharField(null=True, blank=True, max_length=100)
    CNI = models.CharField(null=True, blank=True, max_length=100)
    CNI_recto = models.ImageField(null=True, blank=True, upload_to="CNI/")
    CNI_verso = models.ImageField(null=True, blank=True, upload_to="CNI/")
    about = models.TextField(null=True, blank=True, max_length=1000)

    def __str__(self):
        return f"{self.user.username}"

class Role(models.Model):
    role = models.CharField(max_length=100)
    url = models.CharField(default="#", max_length=30)

    def __str__(self):
    	return f"{self.role}"

class SchoolYear(models.Model):
	start = models.DateField(blank=True, null=True, max_length=100)
	end = models.DateField(blank=True, null=True, max_length=100)
	def __str__(self):
		return f"{self.start} - {self.end}"

