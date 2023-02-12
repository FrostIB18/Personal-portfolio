from django.db import models


class Project(models.Model):
    title = models.CharField(max_length = 100)
    short_description = models.CharField(max_length = 100)
    long_description = models.TextField(default="Here should be a long description.")
    image_1 = models.ImageField(upload_to = 'portfolio/images/')
    image_2 = models.ImageField(upload_to = 'portfolio/images/', blank=True)
    image_3 = models.ImageField(upload_to = 'portfolio/images/', blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title