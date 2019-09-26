from django.db import models
from datetime import datetime


class Deal(models.Model):
    provider = models.CharField(max_length=200, blank=True)
    destination = models.CharField(max_length=200, blank=True)
    details = models.CharField(null=True, max_length=200)
    trip_id = models.URLField(max_length=128, db_index=True,
                              blank=True)
    description = models.TextField(blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.details
