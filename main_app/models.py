from django.db import models
from django.urls import reverse
from datetime import date

EVENTS = (
    ('C', 'Clinic'),
    ('R', 'Recording'),
    ('G', 'Gig')
)

# Create your models here.
class Cymbal(models.Model):
    type = models.CharField(max_length=20)
    size = models.IntegerField()
    brand = models.CharField(max_length=20)
    description = models.TextField(max_length=256)
    sold = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('details', kwargs={'cymbal_id': self.id})

    def __self__(self):
        return f"{self.size} inch {self.brand} {self.type}"

class Hire(models.Model):
    date = models.DateField('Hire Date')
    event = models.CharField(max_length=1,
                             choices=EVENTS,
                             default=EVENTS[0][0]
                             )
    cymbal = models.ForeignKey(Cymbal, on_delete=models.CASCADE) # ensures if the parent is deleted related child are deleted
    # joins or references the cymbal model

    def __str__(self):
        return f"{self.get_event_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']