from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/cv_form', methods=['GET','POST'])
def cv_form():
    if request.method == 'GET':
        return render_template('cv_form.html')
    if request.method == 'POST':
        update={
            #personal information
            'name': request.form['name'],
            'dob' : request.form['dob'],
            'address' : request.form['address'],
            'email': request.form['email'],
            'phone': request.form['phone'],
            #job
            'job-title': request.form['job-title'],
            'company': request.form['company'],
            'job-time': request.form['job-time'],
            'job-desc': request.form['job-desc'],
            
            'keyskill': request.form['keyskill'],
            'school': request.form['school'],
            'qualification': request.form['qualification'],
            'edu-desc': request.form['edu-desc']
        }
        return render_template('updated_template.html',update=update)

    return render_template('main.html')

@app.route('/cv')
def cvtemp1():
    return render_template('Template 1.html')

@app.route('/create')
def create():
        return render_template('Template 2.html')



if __name__ == '__main__':
    app.run()
