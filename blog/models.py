from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now) #auto_now -> will update time when post was modified , auto_now_add -> will add only time when post was created
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    #python manage.py sqlmigrate blog 0001 -> to run migration file with sql
    #puthon3 manage.py shell -> to run python shell

    def __str__(self):
        return self.title
    # redirect will redirec you to specific route
    #reverse will return url to that template as a string

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
