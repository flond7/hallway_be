from django.db import models
from api_user.models import PAUser, PAOffice

# Create your models here.

class goalPeg(models.Model):
 
  year = models.IntegerField(blank=True)
  #office = models.CharField(max_length = 10, blank=True)
  office = models.ForeignKey(
    PAOffice,
    related_name="goal_office",    # used when sending the id in post or put. Django creates that in aut mode with the model name and _set so if you have multiple foreignKeys or ManyToMany it's better to custom name them to avoid conflicts
    on_delete=models.PROTECT,      # prevents from deleting the PAUser linked here
  )
  name = models.CharField(max_length = 500, blank=True)
  description = models.CharField(max_length = 600, blank=True)
  weight = models.IntegerField()
  manager = models.ForeignKey(
    PAUser,
    related_name="goal_manager",  # used when sending the id in post or put. Django creates that in aut mode with the model name and _set so if you have multiple foreignKeys or ManyToMany it's better to custom name them to avoid conflicts
    on_delete=models.PROTECT,      # prevents from deleting the PAUser linked here
  )
  percent_3006 = models.IntegerField()
  weight_3006 = models.IntegerField()
  percent_3112 = models.IntegerField()
  weight_3112 = models.IntegerField()
  type = models.CharField(max_length = 13, blank=False)
  involvedPeople = models.ManyToManyField(
    PAUser, 
    related_name="goal_involvedPeople")

  class Meta:
    ordering = []

  def __str__(self):
    return self.name