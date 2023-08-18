from django.db import models

class Book(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='books/', blank=True, null=True)

    def __str__(self):
        return self.title