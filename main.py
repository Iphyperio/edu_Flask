from flask import Flask


app = Flask(__name__)
app.debug=True

#http://127.0.0.1:5000/lesson/1/step/3:5
@app.route("/<path:lesson>")
def calculate(lesson):
    x=lesson.split('/')[-2]
    print(x)
    s=['','','']
    operations = ('+', ':', '**', '-', '*') # Используемые арифметические операторы для этого задания
    k=0
    for i in range(len(x)):
        if x[i] not in operations:
            s[0]+=x[i]
        else:
            if x[i+1]=='*':
                s[2]='**'
                i+=1
            else:
                s[2]=x[i]
            s[1]=x[i+1:]
            break
        
    print(s)
    if s[2]=='+': result=int(s[0])+int(s[1])
    if s[2]==':': result=int(s[0])/int(s[1])
    if s[2]=='**': result=int(s[0])**int(s[1])
    if s[2]=='-': result=int(s[0])-int(s[1])
    if s[2]=='*': result=int(s[0])*int(s[1])
    return(str(float(result)))
    
'''@app.route('/test-case')
def index():
    return 'Hello, world'
    #$env:FLASK_APP = "main.py"

@app.route("/index/")
def bindex():
    return "index"

@app.route("/contact/")
def contact():
    return "contact information"
'''