from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('main.html')

@app.route('/cv')
def cv():
    return render_template('Template 1.html')

@app.route('/create')
def create():
        return render_template('Template 2.html')



if __name__ == '__main__':
    app.run()
