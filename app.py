from flask import Flask, render_template, request, redirect
import csv
import datetime

app = Flask(__name__)

@app.route("/")
def index():
    f = open("todos.csv","r",encoding="utf-8")
    todos = csv.reader(f)
   # todos =todos[::-1]
    
    return render_template("index.html", todos=todos)

@app.route("/new")
def new():
    return render_template("new.html")
   

@app.route("/create")
def create():
    title = request.args.get("title")
    content = request.args.get("content")
    now = datetime.datetime.now()
    
    f = open("todos.csv","a+",encoding="utf-8",newline="")
    csv_w = csv.writer(f)
    csv_w.writerow([title, content, now])
    f.close()
    
    return redirect('/')
    # return render_template("create.html",title=title,content=content)
    
@app.route('/post_new')
def post_new():
    return render_template("post_new.html")
    
@app.route('/post_create', methods=["post"]) #폼에 저장됨
def post_create():
    title = request.form.get("title")
    content = request.form.get("content")
    now = datetime.datetime.now()
    f2 = open("todos.csv","a+",encoding="utf-8",newline="")
    csv_w = csv.writer(f2)
    csv_w.writerow([title, content, now])
    f2.close
    
    return redirect('/')
    #return render_template("post_create.html")
    
    
if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=8080)