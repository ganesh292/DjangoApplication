# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class score(models.Model):
    score_input = models.IntegerField()
    user=models.ForeignKey(User)

