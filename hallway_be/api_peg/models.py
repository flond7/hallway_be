from django.db import models
from api_user.models import PAUser

# Create your models here.

class goalPeg(models.Model):
 
  year = models.CharField(max_length = 10, blank=True)
  office = models.CharField(max_length = 10, blank=True)
  name = models.CharField(max_length = 10, blank=True)
  descripition = models.CharField(max_length = 600, blank=True)
  weight = models.IntegerField()
  #manager = models.CharField(max_length = 40, blank=True)
  manager = models.ForeignKey(
    PAUser,
    related_name="goal_manager",  # name that identifies the relationship. Django creates that in aut mode with the model name and _set so if you have multiple foreignKeys or ManyToMany it's better to custom name them to avoid conflicts
    on_delete=models.PROTECT,      # prevents from deleting the PAUser linked here
  )
  percent_3006 = models.IntegerField()
  weight_3006 = models.IntegerField()
  percent_3112 = models.IntegerField()
  weight_3112 = models.IntegerField()
  involvedPeople = models.ManyToManyField(
    PAUser, 
    related_name="goal_involvedPeople")

  class Meta:
    ordering = []

  def __str__(self):
    return self.name