from django.db import models
from .province import Province
from django.utils.text import slugify
from django.utils import timezone

class Cni(models.Model):
	cni = models.CharField(max_length=100)

	def __str__(self):
		return f"{self.cni}"
