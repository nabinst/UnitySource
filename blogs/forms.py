
from django import forms
from tinymce.widgets import TinyMCE
from .models import Comment, Post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        #fields = '__all__'


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False

class BlogForm(forms.ModelForm):
    content = forms.CharField(
        widget=TinyMCEWidget(
            attrs={'required': False, 'cols':30, 'rows':10}
        )
    )
    class Meta:
        model = Post
        fields = ['title','overview', 'content','thumbnail', 'categories','featured','previous_post',
'next_post']
