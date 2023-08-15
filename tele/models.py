from django.db import models
from django.utils import timezone
import datetime

class tele_class(models.Model):
    name = models.CharField(max_length=60)
    post_header = models.CharField(max_length=80)
    post_content = models.CharField(max_length=240)
    post_date = models.DateTimeField(auto_now_add=True)
