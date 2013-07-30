from django.db import models

# Create your models here.

class Goal(models.Model):
	title = models.CharField(max_length=256)
	created_at = models.DateTimeField(auto_now_add=True)
	modified_at = models.DateTimeField(auto_now=True)

class CheckmarkLog(models.Model):
	



