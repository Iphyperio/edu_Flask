from flask  import Flask, render_template
app = Flask(__name__)
app.debug=1
print('hello')
@app.route("/<float:n1>/<string:operation>/<float:n2>/")
def index(n1,operation,n2):
    print(n1,n2,operation)
    return render_template('calc.html',
                            n1=n1,
                            n2=n2,
                            operation=operation,
                            )
    '''
   
        '''
if __name__ == '__calculator__':
    app.run(debug=True)
    