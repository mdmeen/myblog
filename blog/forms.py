from django import forms
from .models import post

class postForm(forms.ModelForm) :
    class Meta:
        Model= post
        fields= ('title','content')