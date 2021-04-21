from django.forms import ModelForm, TextInput, Textarea
from .models import Snippet

class SnippetForm(ModelForm):
	class Meta:
		model = Snippet
		fields = ['blogname','blogauth','blogdes', 'img']
		widgets = {
		"blogname":TextInput(attrs={
			'class': 'form-control',
			'placeholder':'Name'
			
			}),
		"blogauth":TextInput(attrs={
			'class': 'form-control',
			'placeholder':'Blogauth'
			
			}),
		"blogdes":Textarea(attrs={
			'class': 'form-control',
			'placeholder':'Input Text'
			
			})
		}