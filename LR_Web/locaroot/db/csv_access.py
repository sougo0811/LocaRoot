import datetime
from flask import Flask,request
app = Flask(__name__)

@app.route('/')
def hello():
  name = "This is CSV server"
  return name

@app.route('/hello')
def good():
    name = "Hello World"
    return name

@app.route('/CSV_ACCESS',methods=["GET","POST"])
def file():
  out = 'CSV_ACCESS'
  if request.method == "POST":
    author = request.json["author"]
    question_title = request.json["question_title"]
    name = request.json["name"]
    answer = str(request.json["answer"])
    dt_now = datetime.datetime.now()
    dt_now = str(dt_now.replace(microsecond = 0))
    path = './' + author + '/' + question_title + '.csv' # ← ここにファイルを指定
    with open(path, 'a', encoding='utf-8') as f:
      f.write(dt_now + ',')
      f.write(author + ',')
      f.write(question_title + ',')
      f.write(name + ',')
      f.write(answer + '\n')
    out = 'CSV ACCESS OK '
  return out

if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')
