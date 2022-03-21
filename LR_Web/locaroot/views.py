from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import QuizModel
from .forms import QuestionForm
from django.contrib.auth.models import User

def index(request):
  return render(request, 'locaroot/index.html', {})

def questions_list(request):
  questions = QuizModel.objects.filter(created_date__lte=timezone.now(), author=request.user.id).order_by('question_id')
  return render(request, 'locaroot/questions_list.html', {'questions': questions})

def question_detail(request, pk):
  question = get_object_or_404(QuizModel, pk=pk)
  return render(request, 'locaroot/question_detail.html', {'question': question})

def question_new(request):
  if request.method == "POST":
    form = QuestionForm(request.POST)
    if form.is_valid():
      question = form.save(commit=False)
      question.author = request.user
      question.created_date = timezone.now()
      #print(type(question.created_date))
      #question.published_date = timezone.now()
      question.save()
      return redirect('question_detail', pk=question.pk)
  else:
    form = QuestionForm()
    return render(request, 'locaroot/question_edit.html', {'form': form})

def question_edit(request, pk):
  question = get_object_or_404(QuizModel, pk=pk)
  if request.method == "POST":
    form = QuestionForm(request.POST, instance=question)
    if form.is_valid():
      question = form.save(commit=False)
      question.author = request.user
      question.created_date = timezone.now()
      #question.published_date = timezone.now()
      question.save()
      return redirect('question_detail', pk=question.pk)
  else:
    form = QuestionForm(instance=question)
  return render(request, 'locaroot/question_edit.html', {'form': form})

def question_delete(request,pk):
  question = get_object_or_404(QuizModel, pk=pk)
  question.delete()
  print("削除完了")
  questions = QuizModel.objects.filter(created_date__lte=timezone.now(), author=request.user.id).order_by('question_id')
  return render(request, 'locaroot/questions_list.html', {'questions': questions})


def answers_list(request):
  answers = QuizModel.objects.filter(published_date__lte=timezone.now(), author=request.user.id).order_by('question_id')
  return render(request, 'locaroot/answers_list.html', {'answers': answers})


from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import(LoginView, LogoutView)
from .forms import LoginForm


class Login(LoginView):
    #ログインページ
    form_class = LoginForm
    template_name = 'accounts/login.html'


class Logout(LoginRequiredMixin, LogoutView):
    #ログアウトページ
    template_name = 'locaroot/index.html'

