from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    # this will be a character field
    title = models.CharField(max_length=100)
    # this is a text field
    content = models.TextField()
    # this is a date field
    datePosted = models.DateTimeField(default=timezone.now)
    # this is a foreign key field
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # create dunder (double underscore) str method for how we want post to look when printed
    def __str__(self):
        return self.title

    # create method to return the url to the post detail page
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    # def save(self):
    #     super().save()
