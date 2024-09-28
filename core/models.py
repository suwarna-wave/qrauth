from django.db import models

# Create your models here.
class ScannedQR(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    event_day = models.CharField(max_length=10)
    event_name = models.CharField(max_length=100)