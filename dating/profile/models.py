from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    friends = models.ManyToManyField('Profile', symmetrical=True,
                                       related_name='friends', blank=True)
    # picture = models.ImageField(
    #       upload_to='photos/', null=True, blank=True)
    bio = models.CharField(max_length=64, blank=True, null=True)
    slug = models.SlugField(max_length=32, unique=True, blank=False, null=True)

    def __str__(self):
        return self.user.username

    def save(self):
        self.slug = slugify(self.user.username)
        super(Profile, self).save()


class Woman(Profile):
    requested_friends = models.ManyToManyField('Profile',
                                               symmetrical=False,
                                               related_name='requesting_friend',
                                               blank=True)

class Man(Profile):
    pass
