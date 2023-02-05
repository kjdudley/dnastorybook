from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='project/images', null=True)
    url = models.URLField(blank=True)
    created = models.DateField(auto_now_add=True)
    datecompleted = models.DateField(null=True, blank=True)
    public = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
