from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.
class post(models.Model):
    title = models.CharField(max_length = 200)
    body = models.TextField()
    created_at = models.DateTimeField(default = datetime.now, blank = True)
    def __str__(self):
        return self.title + " " + '(' + str(self.created_at) + ')'

class Comment(models.Model):
    name = models.CharField(max_length = 20)
    comment = models.TextField()
    date_added = models.DateTimeField(default = timezone.now)
    def __str__(self):
        return self.name + " " + '(' + str(self.id) + ')'
