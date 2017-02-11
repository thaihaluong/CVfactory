from flask import Flask, render_template, request, url_for

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('cv_maker.html')

@app.route('/cv_form1', methods=['GET','POST'])
def cv_form1():
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

            #education
            'school-time' : request.form['school-time'],
            'school': request.form['school'],
            'qualification': request.form['qualification'],
            'edu-desc': request.form['edu-desc']
        }
        return render_template('updated_template1.html', update=update)

    return render_template('main.html')

@app.route('/template1')
def template1():
    return render_template('template1.html')

@app.route('/template2')
def template2():
        return render_template('template2.html')


@app.route('/cv_form2', methods=['GET','POST'])
def cv_form2():
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

            #education
            'school-time' : request.form['school-time'],
            'school': request.form['school'],
            'qualification': request.form['qualification'],
            'edu-desc': request.form['edu-desc']
        }
        return render_template('updated_template2.html', update=update)


if __name__ == '__main__':
    app.run(port=6979)
