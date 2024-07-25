from django.db import models

# Create your models here.


class BlogPost(models.Model):
    title = models.CharField(max_length = 500)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    date = models.DateField()

    def __str__(self):
        return self.title