from django.db import models
from django.utils.text import slugify
from django.shortcuts import reverse
from time import time

# Create your models here.


def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug + '-' + str(int(time()))


class ImageTag(models.Model):
    slug = models.SlugField(max_length=15, unique=True)
    image = models.ImageField(upload_to='images/', blank=True)

    def get_absolute_url(self):
        return reverse('tag_detail_url', kwargs={'slug': self.slug})


    def __str__(self):
        return self.slug

    class Meta:
        ordering = ['slug']


class Post(models.Model):
    title = models.CharField(max_length=40, db_index=True)
    slug = models.SlugField(max_length=50, unique=True)
    project_image = models.ImageField(upload_to='images/', blank=True)
    technologists = models.ManyToManyField('ImageTag', blank=True, related_name='tags')
    description = models.CharField(max_length=200, blank=True)
    programme_language = models.CharField(max_length=40, blank=True)
    update_time = models.CharField(max_length=40, blank=True)
    link = models.URLField()
    pin = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Gettign the absolute url of index.html"""

        return reverse('project_detail_url', kwargs={'slug': self.slug})

    def get_update_url(self):

        return reverse('project_edit_url', kwargs={'slug': self.slug})

    def get_delete_url(self):

        return reverse('project_delete_url', kwargs={'slug': self.slug})

    def get_image_url(self):
        return reverse('add_project_image_url', kwargs={'slug': self.slug})

    def get_technology_url(self):
        return reverse('add_technology_url', kwargs={'slug': self.slug})

    def pin_post_url(self):
        return reverse('pin_post_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        """Complement the method save of django Model"""
        # if not self.id:
        #     self.slug = gen_slug(self.title)

        if not self.slug:
            self.slug = gen_slug(self.title)

        if self.slug:
            checker = self.slug.strip()
            if checker:
                pass
            else:
                self.slug = gen_slug(self.title)

        super().save(*args, **kwargs)

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


class Email(models.Model):
    slug = models.SlugField(max_length=30, unique=True, blank=True)
    email = models.EmailField(max_length=30, blank=True)
    email_password = models.CharField(max_length=50, blank=True)
    email_host = models.CharField(max_length=20, blank=True)
    email_port = models.CharField(max_length=20, blank=True)
    email_ssl = models.BooleanField(default=True, blank=True)
    email_tls = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return self.slug

    def get_email_update_ulr(self):
        return reverse('email_setting_url', kwargs={'slug': self.slug})


class GitHubProfile(models.Model):
    slug = models.SlugField(max_length=30, unique=True, blank=True)
    link = models.URLField()

    def __str__(self):
        return self.slug

    def get_github_update_url(self):
        return reverse('github_setting_url', kwargs={'slug': self.slug})