from django.db import models

class Category(models.Model):
	category = models.TextField(max_length=100)

	def __str__(self):
		return self.category