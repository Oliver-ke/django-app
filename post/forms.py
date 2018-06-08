# here a class represents something in html, just like in models a class represents something in the database
# so here we are creating classes to map html inputs 
from django import forms

class CommentForm(forms.Form):
    name = forms.CharField(max_length=20,
            widget = forms.TextInput(attrs= {'class': 'field-wrap' }))
    comment = forms.CharField(
    	widget = forms.Textarea(attrs= {'class': 'field-wrap' }) )