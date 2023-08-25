from django.db import models

# Create your models here.

class accessoAtti(models.Model):
 
  requestProtocol = models.CharField(max_length = 10, blank=True)
  requestDate = models.CharField(max_length = 20, blank=True)
  requestApplicant = models.CharField(max_length = 80, blank=True)
  accesstype = models.CharField(max_length = 80, blank=True)
  topic = models.TextField(default="", blank=True)
  others = models.CharField(max_length = 20, blank=True)
  responsable = models.CharField(max_length = 40, blank=True)
  answerResult = models.CharField(max_length = 20, blank=True)
  answerProtocol = models.CharField(max_length = 10, blank=True)
  answerDate = models.CharField(max_length = 20, blank=True)
  answerNote = models.TextField(default="", blank=True)

  class Meta:
    ordering = []

  def __str__(self):
    return 'Richiesta protocollo' + self.requestProtocol + ' del ' + self.requestDate
