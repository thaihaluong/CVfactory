from flask import Flask, render_template, request, url_for

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('template.html')

@app.route('/cv_form', methods=['GET','POST'])
def cv_form():
    if request.method == 'GET':
        return render_template('cv_form.html')
    if request.method == 'POST':
        update={
            'name': request.form['name'],
            'job-title-main': request.form['job-title-m'],
            'email': request.form['email'],
            'website': request.form['website'],
            'phone': request.form['phone'],
            'profile-desc': request.form['profile-desc'],
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



if __name__ == '__main__':
    app.run()
