from django.db import models
from api_user.models import PAUser

# Create your models here.

class obbiettivo(models.Model):
 
  year = models.CharField(max_length = 10, blank=True)
  office = models.CharField(max_length = 10, blank=True)
  name = models.CharField(max_length = 10, blank=True)
  descripition = models.CharField(max_length = 600, blank=True)
  weight = models.IntegerField()
  responsable = models.CharField(max_length = 40, blank=True)
  completation3006 = models.IntegerField()
  completation3112 = models.IntegerField()
  people = models.ManyToManyField(PAUser)

  class Meta:
    ordering = []

  def __str__(self):
    return self