from django.db import models
from django.utils.text import slugify
from django.shortcuts import reverse
from time import time

# Create your models here.


class ImageTag(models.Model):
    slug = models.SlugField(max_length=15, unique=True)
    image = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.slug


class Post(models.Model):
    title = models.CharField(max_length=40, db_index=True)
    project_image = models.ImageField(upload_to='images/', blank=True)
    technologists = models.ManyToManyField('ImageTag', blank=True, related_name='tags')
    description = models.CharField(max_length=200, blank=True)
    programme_language = models.CharField(max_length=40, blank=True)
    update_time = models.CharField(max_length=40, blank=True)
    link = models.URLField()
    pin = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return self.title

    def reduction_description(self):
        """Cut the project description"""
        reduction = '' # a part of project description
        steps = 0
        for i in range(len(self.description)):
            if steps == 7:
                break
            elif self.description[i] == ' ':
                steps += 1
                reduction += self.description[i]
            else:
                reduction += self.description[i]

        reduction += '...'
        return reduction
