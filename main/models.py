from django.db import models


# Create your models here.
class Books(models.Model):
    title = models.CharField('Name book', max_length=50)
    about_book = models.TextField('About book')

    def __str__(self):
        return self.title