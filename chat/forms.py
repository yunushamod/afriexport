from django import forms
from django import forms

class MessageForm(forms.Form):
    message = forms.CharField(max_length=400, widget=forms.Textarea, required=True)