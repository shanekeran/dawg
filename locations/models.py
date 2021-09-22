from django.db import models


class Location(models.Model):
    city = models.CharField(max_length=300, null=False, blank=False)
    address = models.CharField(max_length=500, null=False, blank=False)
    phone_number = models.IntegerField(null=False, blank=False)
    opening_hours = models.CharField(max_length=300, null=False, blank=False)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.city