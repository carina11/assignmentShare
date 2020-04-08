from flask import Flask, render_template, request
import subprocess
import os
#from datetime import datetime
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

    print(deadline)
    print(assignmentName)
    if(os.path.isdir("assignment") == False):
        os.mkdir("assignment")

    assignmentPath = 'assignment/' + time +".txt"
    f = open(assignmentPath, 'w')
    f.write(deadline)
    f.write(" ")
    f.write(assignmentName)
    f.close()
    print("処理完了")
    return render_template("uploadSuccess.html")
    

if __name__ == "__main__":
    app.run(debug=True)