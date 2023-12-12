# myportfolio/forms.py

# Import forms
from django import forms

class ContactForm(forms.Form):
    """Form for handling contact submissions."""
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
