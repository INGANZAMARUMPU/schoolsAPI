from django.db import models
from .province import Province
from django.utils.text import slugify
from django.utils import timezone

class SearchUser(models.Model):
	search_user = models.TextField(max_length=100)

	def __str__(self):
		return f"{self.search_user}"
