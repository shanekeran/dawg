from django.db import models


class Contact(models.Model):
    """Saves a contact model in database."""

    full_name = models.CharField(max_length=200, null=False, blank=False)
    email_address = models.CharField(max_length=200, null=False, blank=False)
    subject = models.CharField(max_length=50, null=False, blank=False)
    message = models.TextField()
    date_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
