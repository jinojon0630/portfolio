from django.db import models
from datetime import date

class Blog(models.Model):
    title = models.CharField(max_length = 100)
    pub_date = models.DateTimeField()
    body = models.TextField(max_length = 800)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:150]
    
    def date_format(self):
        return self.pub_date.strftime('%b %e %Y')