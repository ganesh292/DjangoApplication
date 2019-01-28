# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    post = models.CharField(max_length=3)
    user=models.ForeignKey(User,on_delete=models.DO_NOTHING,)

