from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text', 'group')
        labels = {
            'text': 'Введите текст',
        }
        help_texts = {
            'text': '(Поле обязательно для заполнения)',
        }
