from flask  import Flask, render_template
from random import choice, randint, random
random_name= choice(['Serj','Bob','Jimmy','Arny','Sveta'])
project_number=randint(1,100)
app = Flask(__name__)
app.debug=1

@app.route("/")
def index():
    return render_template('index.html',
                            name='testPage',
                            title='Home page',
                            project_name=random_name,
                            project_number=project_number
                            )
    '''
   
        '''
if __name__ == '__main__':
    app.run(debug=True)
    