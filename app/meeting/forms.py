from django import forms
from django.forms import ModelForm, ChoiceField, Form
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User

from models import Meeting

class MeetingForm (ModelForm):

    class Meta:
        model = Meeting
        fields = ('title', 'purpose', 'length_in_minutes',)

    title = forms.CharField(max_length=255, label = "Title :")
    purpose = forms.CharField(widget=forms.Textarea, label = "Purpose :")
    length_in_minutes = forms.ChoiceField(label="Length: ", choices=((10, '10 minutes'), (20, '20 minutes'),(30, '30 minutes'), (45, '45 minutes'), (60, '1 hour'),))