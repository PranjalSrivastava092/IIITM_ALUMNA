# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Event(models.Model):
	title = models.CharField(max_length=80)
	content = models.TextField()
	time = models.DateTimeField(auto_now=True, aut_now_add=False)
	

