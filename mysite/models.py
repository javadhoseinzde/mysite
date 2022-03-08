from django.db import models


class Article(models.Model):
	title = models.CharField(max_length=100)
	slug = models.SlugField(max_length=100, unique=True, null=True)
	description = models.TextField()
	status = models.BooleanField(default=False)
	time = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.title

class info(models.Model):
	name = models.CharField(max_length=100)
	pic = models.ImageField(upload_to="media/")
	slug = models.SlugField(max_length=100, unique=True, null=True)
	description = models.TextField()
	skils = models.CharField(max_length=100, blank=True)
	skils1 = models.CharField(max_length=100, blank=True)
	skils2 = models.CharField(max_length=100, blank=True)
	skils3 = models.CharField(max_length=100, blank=True)
	skils4 = models.CharField(max_length=100, blank=True)
	skils5 = models.CharField(max_length=100, blank=True)
	skils6 = models.CharField(max_length=100, blank=True)
	skils7 = models.CharField(max_length=100, blank=True)
	skils8 = models.CharField(max_length=100, blank=True)
	skils9 = models.CharField(max_length=100, blank=True)
	skils10 = models.CharField(max_length=100, blank=True)
	skils11 = models.CharField(max_length=100, blank=True)
	skils12 = models.CharField(max_length=100, blank=True)

	def __str__(self):
		return self.name