from django.db import models

# Create your models here.
class Users(models.Model):
    id = models.AutoField(auto_created=False, primary_key=True, serialize=False,verbose_name="ID")
    title = models.CharField('Name book', max_length=50)
    about_book = models.TextField('About book')

    def __str__(self):
        return self.title