from django import forms
from .models import Question

class QuestionForm(forms.ModelForm):
  class Meta:
    model = Question
    fields = ['subject', 'content']
    # template에서 직접 디자인하기 위해 widgets 항목 제거
    # widgets = {
    #   'subject': forms.TextInput(attrs={'class': 'form-control'}),
    #   'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
    # }
    labels = {
      'subject': '제목',
      'content': '내용',
    }

from .models import Answer
class AnswerForm(forms.ModelForm):
  class Meta:
    model = Answer
    fields = ['content']
    labels = {
      'content': '답변내용',
    }