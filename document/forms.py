from django.forms import ModelForm
from .models import DocumentComment, Document


class CommentForm(ModelForm):
    class Meta:
        model = DocumentComment
        fields = ['comment']
        labels = {'comment': ""}


class ControlForm(ModelForm):
    class Meta:
        model = Document
        fields = []