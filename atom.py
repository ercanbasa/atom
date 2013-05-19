from django.db import models

class Atom(models.Model):
	runs_under_water = models.BooleanField(default=True)
