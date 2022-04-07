""" Libraries """
from django import forms
from .models import Post, Category, Comment

choices = Category.objects.all().values_list('name', 'name')

choice_list = []

for item in choices:
    choice_list.append(item)


class PostForm(forms.ModelForm):
    """ this will help to shape the add post form """
    class Meta:
        """ This will help to edit the form """
        model = Post
        fields = ('post_title', 'author', 'category', 'image', 'content')
        widgets = {
            'post_title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'identifier', 'type': 'hidden'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            }


class EditForm(forms.ModelForm):
    """ This will help to share the edit post form """
    class Meta:
        """ stle the form """
        model = Post
        fields = ('post_title', 'category', 'image', 'content')
        widgets = {
            'post_title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }


class CommentForm(forms.ModelForm):
    """ It will help to shape the add a comment form """
    class Meta:
        """ giving some style to the form """
        model = Comment
        fields = ('name', 'body')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            }
