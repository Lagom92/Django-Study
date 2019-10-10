from django.db import models

class Hobby(models.Model):
    title = models.CharField(max_length=30)
    maker = models.CharField(max_length=15)
    content = models.TextField()

    def __str__(self):
        return self.title
