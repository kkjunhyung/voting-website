from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.title