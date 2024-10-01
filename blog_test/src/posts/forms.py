from django import forms
from posts.models import BlogPost

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'created_on', 'published']
        widgets = {
            'created_on': forms.DateInput(attrs={'type': 'date'}),  # Utilisation d'un champ de type date
        }
