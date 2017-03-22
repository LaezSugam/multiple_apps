from __future__ import unicode_literals

from django.db import models
from ..log_reg.models import Users

# Create your models here.
class Courses(models.Model):
    course_name = models.CharField(max_length=255)
    user = models.ManyToManyField(Users, related_name="course_users")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Descriptions(models.Model):
    description = models.TextField()
    course = models.OneToOneField(Courses, related_name="course_description")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comments(models.Model):
    comment = models.TextField()
    course = models.ForeignKey(Courses)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
