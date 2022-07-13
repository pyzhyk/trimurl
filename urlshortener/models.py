from django.db import models
from .utils import create_shortened_url
from django.contrib.auth.models import User


class Shortener(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	long_url = models.URLField()
	short_url = models.CharField(max_length=15, unique=True, blank=True)
	author = models.ForeignKey(User,on_delete=models.CASCADE)
	follows = models.PositiveIntegerField(default=0)

	class Meta:
		ordering = ["-created"]

	def __str__(self):
		return f'{self.long_url} to {self.short_url}'

	def save(self, s=False, *args, **kwargs):
		# If the short url wasn't specified
		if not self.short_url:
			# We pass the model instance that is being saved
			self.short_url, s = create_shortened_url(self)
		if s:
			super().save(*args, **kwargs)
