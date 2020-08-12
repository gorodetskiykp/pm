from django.forms import ModelForm
from .models import DocumentComment

class CommentForm(ModelForm):
    class Meta:
        model = DocumentComment
        fields = ['comment']
        labels = {'comment': ""}
