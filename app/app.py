from flask import Flask, render_template, request
import subprocess
import os
import datetime

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("Assignment_List.html")

@app.route("/upload", methods=["POST"])
def upload():
    deadline = request.form['deadline']
    assignmentName = request.form['assignmentName']
    time = request.form['time']
    subject = request.form['subject']

    if(os.path.isdir("deadline") == False):
        os.mkdir("deadline")
    if(os.path.isdir("assignmentName") == False):
        os.mkdir("assignmentName")
    if(os.path.isdir("subject") == False):
        os.mkdir("subject")

    

    f = open('subject/'+ time, 'w')
    f.write(subject)
    f.close()

    f = open('assignmentName/'+time, 'w')
    f.write(assignmentName)
    f.close()

    f = open('deadline/'+time, 'w')
    f.write(deadline)
    f.close()

    return render_template("uploadSuccess.html")

@app.route("/table")
def table():
    if(os.path.isdir("deadline") == False):
        os.mkdir("deadline")
    if(os.path.isdir("assignmentName") == False):
        os.mkdir("assignmentName")
    if(os.path.isdir("subject") == False):
        os.mkdir("subject")
    cmd = 'ls subject/'
    out = subprocess.check_output(cmd.split()).decode('utf-8')
    out_list = out.split()
    length = len(out_list)

    array = []
    i = 0
    while (i < length):
        f = open('subject/'+out_list[i], "r")
        array.append(f.read())
        f.close()
        f = open('assignmentName/'+out_list[i], "r")
        array.append(f.read())
        f.close()
        f = open('deadline/'+out_list[i], "r")
        array.append(f.read())
        f.close()
        i = i + 1

    return render_template("table.html", list = out_list, array = array, length=length)
    

if __name__ == "__main__":
    app.run(debug=True)