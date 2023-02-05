from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=100)
    notetext = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    project = models.CharField(max_length=100, blank=True)
    area = models.CharField(max_length=100, blank=True)
    source = models.URLField(blank=True)
    archive = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
