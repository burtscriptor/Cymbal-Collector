from django.db import models

# Create your models here.
class Cymbal(models.Model):
    type = models.CharField(max_length=20)
    size = models.IntegerField()
    brand = models.CharField(max_length=20)
    description = models.TextField(max_length=256)
    sold = models.BooleanField(default=False)

    def __self__(self):
        return f"{self.size} inch {self.brand} {self.type}"

