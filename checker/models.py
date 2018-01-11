
from django.db import models
from django.contrib.auth.models import User



class Data(models.Model):
	data = models.TextField()
	user = models.ForeignKey(User)


class Document(models.Model):
	document = models.FileField(upload_to="documents/")
	description = models.CharField(max_length=255, blank=True)
	# keywords = models.CharField(max_length=500)
