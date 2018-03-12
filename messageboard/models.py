from django.db import models
from django.utils import timezone


class mess(models.Model):
	username = models.TextField(default="human :D")
	content = models.TextField(default="I'm contents...")
	date = models.DateTimeField(default=timezone.now())

	def __str__(self):
		return self.content
		
