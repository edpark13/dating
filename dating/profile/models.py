from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# Create your models here.
class Profile(models.Model):
  user = models.OneToOneField(User, related_name='profile')
  friends = models.ManyToManyField('Profile', symmetrical=True,
                                     related_name='friends', null=True,
                                     blank=True)
  # picture = models.ImageField(
  #       upload_to='photos/', null=True, blank=True)
  bio = models.CharField(max_length=64, blank=True, null=True)


class Woman(Profile):
  requested_friends = models.ManyToManyField('Profile',
                                             symmetrical=False,
                                             related_name='requesting_friend',
                                             null=True, blank=True)

class Man(Profile):
  pass
