from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Video_Url(models.Model):
    vid_id = models.CharField(max_length=10,unique=True)
    vid_url = models.CharField(max_length=100)

    def __str__(self):
        return self.vid_id
