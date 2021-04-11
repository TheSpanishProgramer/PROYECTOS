from django import forms

from .models import MagazineApp

class StoryForm(forms.ModelForm):
    class Meta:
        model = MagazineApp
        fields = [
            'title',
            'synopsis',
            'author',
            'genre',
        ]