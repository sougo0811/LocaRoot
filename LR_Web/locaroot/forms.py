from django import forms
from django.utils import timezone
from .models import QuizModel
from django.contrib.auth.forms import AuthenticationForm 

class QuestionForm(forms.ModelForm):

    class Meta:
        model = QuizModel
        fields = ('question_title', 'question_id', 'question', 'answer_num', 'answer')
        labels = {
            'question_title': '問題名', 
            'question_id': '問題番号', 
            'question': '問題', 
            'answer_num': '解答番号', 
            'answer':'解答',
        }

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label