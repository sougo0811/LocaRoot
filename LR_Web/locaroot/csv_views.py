import csv
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import QuizModel
import os

#データベースアクセスパス
path = "locaroot/db/"

#ユーザー名
user_name = ""

#ファイル名
file_name = ""

# 

def csv_make(request,pk):
  question = get_object_or_404(QuizModel, pk=pk)
  if request.method == 'POST':
    question_item = request.POST.getlist("question")
    print(question.published_date)
    question.published_date = timezone.now()
    question.save()
    print(question_item)
    sheet_author = question_item[7]
    sheet_title = question_item[1]
    question_id = question_item[2]
    user_name = sheet_author
    #csv_files = os.listdir(path)
    dirnames = os.listdir(path)
    file_name = sheet_title + ".csv"
    print(dirnames)
    if user_name not in dirnames:
      os.mkdir(path+user_name)
    with open(path + user_name + "/" + file_name, 'w') as csv_file_f:
      field_names = ["受信時刻","問題作成者名", "問題名","回答者名","回答番号"]
      writer = csv.DictWriter(csv_file_f, fieldnames=field_names)
      writer.writeheader()
  questions = QuizModel.objects.filter(created_date__lte=timezone.now(), author=request.user.id).order_by('question_id')
  return render(request, 'locaroot/questions_list.html', {'questions': questions})

def csv_read(request,pk):
  question = get_object_or_404(QuizModel, pk=pk)
  user_name = question.author
  file_name = question.question_title
  #print(str(user_name))
  csv_answers = []
  with open(path + str(user_name) + "/" + file_name + ".csv", 'r', encoding='Shift_JIS') as csv_file_f:
    csvreader = csv.reader(csv_file_f)
    for row in csvreader:
      print(row)
      csv_answers.append(row)
  #csv_answers = {'lists': csv_answers}
  csv_answers_title = csv_answers[0]
  print(csv_answers)
  print("動作完了")
  return render(request, 'locaroot/answer_detail.html', {'csv_answers': csv_answers})

def answer_analysis(request,pk):
  answer = get_object_or_404(QuizModel, pk=pk)
  user_name = answer.author
  file_name = answer.question_title
  csv_answers = []
  students_answer = []
  names = []
  students_ansewer_data = []
  with open(path + str(user_name) + "/" + file_name + ".csv", 'r', encoding='Shift_JIS') as csv_file_f:
    csvreader = csv.reader(csv_file_f)
    cnt = 0
    for row in csvreader:
      if cnt >= 2:
        student_answer = []
        #print(row)
        student_answer.append(row[0])
        student_answer.append(row[3])
        student_answer.append(row[4])
        students_answer.append(student_answer)
      csv_answers.append(row)
      cnt += 1
  students_answer = sorted(students_answer, reverse=True, key=lambda x: x[0])
  for i in range(len(students_answer)):
    if students_answer[i][1] not in names:
      students_ansewer_data.append(students_answer[i])
      names.append(students_answer[i][1])
  print("------------------------------------------")
  print(students_ansewer_data)
  return render(request, 'locaroot/answer_analysis.html', {'answer': answer})
