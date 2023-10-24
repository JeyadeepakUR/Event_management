from django.db import models
from users.models import CustomUser

class Event(models.Model):
    EVENT_TYPES = (
        ('tech', 'Tech'),
        ('non-tech', 'Non-Tech'),
        ('fest', 'Fest'),
    )

    event_name = models.CharField(max_length=255)
    event_location = models.CharField(max_length=255)
    event_type = models.CharField(max_length=10, choices=EVENT_TYPES)
    event_description = models.TextField()
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    event_banner = models.ImageField(upload_to='uploads/event_banners/') 
    entry_fee = models.DecimalField(max_digits=6, decimal_places=2, default=0.00, null=True, blank=True)
    is_highlight = models.BooleanField(default=False)
    organizer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="events_organized")
    def __str__(self):
        return self.event_name

