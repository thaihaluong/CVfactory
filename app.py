from flask import Flask, render_template, request, url_for
import os

app = Flask(__name__)
app.config['IMAGE_FOLDER'] = os.path.join(os.path.dirname(os.path.abspath(__file__)),'image')

@app.route('/')
def hello_world():
    return render_template("cv_maker.html")

@app.route('/cv_form1', methods=['GET','POST'])
def cv_form_tem1():
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
            #job1
            'job-title1': request.form['job-title1'],
            'company1': request.form['company1'],
            'job-time1': request.form['job-time1'],
            'job-desc1': request.form['job-desc1'],
            #job2
            'job-title2': request.form['job-title2'],
            'company2': request.form['company2'],
            'job-time2': request.form['job-time2'],
            'job-desc2': request.form['job-desc2'],
            #education
            'school-time' : request.form['school-time'],



            'school': request.form['school'],
            'qualification': request.form['qualification'],
            'edu-desc': request.form['edu-desc'],
            #edu1
            'school-time1': request.form['school-time1'],
            'school1': request.form['school1'],
            'qualification1': request.form['qualification1'],
            'edu-desc1': request.form['edu-desc1'],
            #edu2
            'school-time2': request.form['school-time2'],
            'school2': request.form['school2'],
            'qualification2': request.form['qualification2'],
            'edu-desc2': request.form['edu-desc2'],
            #misc
            'img' : request.form['img']
        }
        return render_template('updated_template1.html',update=update)

    return render_template('main.html')

@app.route('/cv')
def cvtemp1():
    return render_template('Template 1.html')

@app.route('/create')
def create():
        return render_template('Template 2.html')


@app.route('/cv_form2', methods=['GET','POST'])
def cv_form_tem2():
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
            #job1
            'job-title1': request.form['job-title1'],
            'company1': request.form['company1'],
            'job-time1': request.form['job-time1'],
            'job-desc1': request.form['job-desc1'],
            #job2
            'job-title2': request.form['job-title2'],
            'company2': request.form['company2'],
            'job-time2': request.form['job-time2'],
            'job-desc2': request.form['job-desc2'],
            #education
            'school-time' : request.form['school-time'],
            'school': request.form['school'],
            'qualification': request.form['qualification'],
            'edu-desc': request.form['edu-desc'],
            #edu1
            'school-time1': request.form['school-time1'],
            'school1': request.form['school1'],
            'qualification1': request.form['qualification1'],
            'edu-desc1': request.form['edu-desc1'],
            #edu2
            'school-time2': request.form['school-time2'],
            'school2': request.form['school2'],
            'qualification2': request.form['qualification2'],
            'edu-desc2': request.form['edu-desc2'],
            #misc
            'img' : request.form['img']}


        return render_template('updated_template2.html', update=update)


if __name__ == '__main__':

    app.run()


