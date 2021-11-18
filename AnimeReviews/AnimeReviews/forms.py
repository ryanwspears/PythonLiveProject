from django.forms import ModelForm
from .models import Anime
from django import forms


class NewAnime(ModelForm):
    class Meta:
        model = Anime
        fields = '__all__'

        widgets = {
            'animeName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Anime Name'}),
            'numOfEpisodes': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Number Of Episodes'}),
            'studioName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Studio Name'}),
            'rating': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Rating(1-10)'}),
            'review': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write Your Review'}),
        }
