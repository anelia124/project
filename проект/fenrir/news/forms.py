from .models import Articles
from django.forms import ModelForm, TextInput, Textarea


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'Full_text', 'date']

        widgets = {
            "title":TextInput (attrs={
                'class':'form-control',
                'placeholder':'Headline'
            }),
            "anons":TextInput (attrs={
                'class':'form-control',
                'placeholder':'Anons'
            }),
            "date":DateTimeInput (attrs={
                'class':'form-control',
                'placeholder':'Date'
            }),
            "Full_text":Textarea (attrs={
                'class':'form-control',
                'placeholder':'Full_text'
            })

        }