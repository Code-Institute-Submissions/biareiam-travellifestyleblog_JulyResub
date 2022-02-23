from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('post_title','author','content')
        widgets = {
            'post_title':forms.TextInput(attrs={'class':'form-control' }),
            'author':forms.TextInput(attrs={'class':'form-control'}),
            #'category': forms.Select(choices=choice_list, attrs={'class':'form-control'}),
            #'featured_image':forms.TextInput(attrs={'class':'form-control'}),
            'content':forms.Textarea(attrs={'class':'form-control'}),
            
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('post_title','content')
        widgets = {
            'post_title':forms.TextInput(attrs={'class':'form-control'}),
            #'featured_image':forms.TextInput(attrs={'class':'form-control'}),
            #'category': forms.Select(choices=choice_list, attrs={'class':'form-control'}),
            'content':forms.Textarea(attrs={'class':'form-control'}),
        }