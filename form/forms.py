# -*- coding: utf-8 -*-
from django import forms # пока не заню для чего
from form.models import Post

class PostForms(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('post_title', 'post_text',)

