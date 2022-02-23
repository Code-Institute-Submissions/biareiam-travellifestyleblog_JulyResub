from django import forms
from .models import Post, Category

choices = Category.objects.all().values_list('name','name')

choice_list = []

for item in choices:
    choice_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('post_title','author','category','image', 'content')
        widgets = {
            'post_title':forms.TextInput(attrs={'class':'form-control' }),
            'author':forms.Select(attrs={'class':'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class':'form-control'}),
            #'featured_image':forms.TextInput(attrs={'class':'form-control'}),
            'content':forms.Textarea(attrs={'class':'form-control'}),
            
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('post_title', 'category', 'image', 'content')
        widgets = {
            'post_title':forms.TextInput(attrs={'class':'form-control'}),
            #'featured_image':forms.TextInput(attrs={'class':'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class':'form-control'}),
            'content':forms.Textarea(attrs={'class':'form-control'}),
        }