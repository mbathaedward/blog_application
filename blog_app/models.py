from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=100)
    status = models.BooleanField(default=False,verbose_name='completed')
    image = models.ImageField(upload_to='posts/', blank=True, null=True)
    date_created = models.DateField()


def __str__(self):
    return self.title
