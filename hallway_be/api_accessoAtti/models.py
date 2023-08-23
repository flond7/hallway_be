from django.db import models

# Create your models here.

class accessoAtti(models.Model):
 
  requestProtocol = models.CharField(max_length = 10, blank=False)
  requestDate = models.CharField(max_length = 20, blank=False)
  requestApplicant = models.CharField(max_length = 80, blank=False)
  accesstype = models.CharField(max_length = 80, blank=False)
  topic = models.TextField(default="", blank=False)
  others = models.CharField(max_length = 20, blank=False)
  responsable = models.CharField(max_length = 40, blank=False)
  answerResult = models.CharField(max_length = 20, blank=False)
  answerProtocol = models.CharField(max_length = 10, blank=False)
  answerDate = models.CharField(max_length = 20, blank=False)
  answerNote = models.TextField(default="", blank=True)

  class Meta:
    ordering = []

  def __str__(self):
    return 'Richiesta protocollo' + self.requestProtocol + ' del ' + self.requestDate
