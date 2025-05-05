from django.db import models
from django.contrib.auth.models import User

class T_Event(models.Model):
  title = models.CharField(max_length=255)
  description = models.CharField(max_length=255)
  date = models.DateTimeField()
  

class T_Participation(models.Model):
  user_id = models.ForeignKey(User, on_delete=models.CASCADE)
  event_id = models.ForeignKey(T_Event, on_delete=models.CASCADE, related_name='participations')

  class Meta:
    unique_together = ('user_id', 'event_id')
