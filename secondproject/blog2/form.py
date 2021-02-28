from django import forms
from .models import Blog

class BlogPost(forms.ModelForm) :#모델을 기반으로한 폼이면 'ModelForm'임의의 입력 폼이면 'Form'#
    class Meta:
        model = Blog
        fields=['title','body']