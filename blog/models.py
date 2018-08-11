from django.db import models
from datetime import date

class Blog(models.Model):
    title = models.CharField(max_length = 100)
    pub_date = models.DateTimeField()
    body = models.TextField(max_length = 500)
    image = models.ImageField(upload_to='images/')
