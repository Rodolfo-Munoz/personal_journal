from django.forms import ModelForm
from .models import Entry

# the classes created here are representations of the html forms and fields
# just like the classes in models are representations of databases tables and rows
# I imported the ModelForm and the Entry class from models

class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = ['title', 'text']


