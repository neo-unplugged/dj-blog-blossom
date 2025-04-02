from django import forms
from .models import Content

class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ['title', 'author', 'content', 'type']

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'block w-full px-4 py-2 border rounded-lg focus:ring-2 focus:ring-pink-400', 
                'placeholder': 'Enter title'
            }),
            'author': forms.TextInput(attrs={
                'class': 'block w-full px-4 py-2 border rounded-lg focus:ring-2 focus:ring-pink-400', 
                'placeholder': 'Author name'
            }),
            'content': forms.Textarea(attrs={
                'class': 'block w-full px-4 py-2 border rounded-lg focus:ring-2 focus:ring-pink-400', 
                'placeholder': 'Write your content here', 
                'rows': 5
            }),
            'type': forms.Select(attrs={
                'class': 'block w-full px-4 py-2 border rounded-lg focus:ring-2 focus:ring-pink-400'
            }),
        }
