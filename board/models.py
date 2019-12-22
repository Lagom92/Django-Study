from django.db import models

class Hobby(models.Model):
    title = models.CharField(max_length=30)
    maker = models.CharField(max_length=15)
    content = models.TextField()

    def __str__(self):
        return self.title

class Paper(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=30)
    contents = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title