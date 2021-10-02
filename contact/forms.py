from django import forms
from .models import Contact


class ContactUs(forms.ModelForm):
    """Creates the Contact Us form"""

    class Meta:
        model = Contact
        fields = (
            'full_name',
            'email_address',
            'subject',
            'message',
            )
