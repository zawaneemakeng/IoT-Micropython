from django.db import models


class TempHumid(models.Model):
    code = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    temperature = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True)  # ไม่บังคับส่งมา
    humidity = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True)  # ไม่บังคับส่งมา
    timestamp = models.DateTimeField(auto_now_add=True)

# Create your models here.
