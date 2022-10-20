from flask  import Flask, render_template
app = Flask(__name__)
app.debug=1

@app.route("/<float:r>/")
def index(r):
    return render_template('equation.html',
                            r=r,
                            pi=3.14
                            )
    '''
   
        '''
if __name__ == '__main__':
    app.run(debug=True)
    