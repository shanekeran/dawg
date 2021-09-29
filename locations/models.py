from django.db import models


class Location(models.Model):
    city = models.CharField(max_length=300, null=False, blank=False)
    address = models.CharField(max_length=500, null=False, blank=False)
    phone_number = models.IntegerField(null=False, blank=False)
    opening_hours = models.CharField(max_length=300, null=False, blank=False)

    def __str__(self):
        return self.city