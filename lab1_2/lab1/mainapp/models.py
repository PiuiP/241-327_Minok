from django.db import models

class Plant(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    height_cm = models.IntegerField()
    is_evergreen = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
      


