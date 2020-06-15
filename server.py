from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def index_route():
    return render_template('index.html')


# @app.route('/<string:page_name>')
# def page_route(page_name):
#     return render_template(page_name)


@app.route('/contact')
def contact_route():
    return render_template('contact.html')


@app.route('/about')
def about_route():
    return render_template('about.html')


@app.route('/works')
def works_route():
    return render_template('works.html')


@app.route('/work')
def work_route():
    return render_template('work.html')


@app.route('/FaceDetectionProject')
def project1_route():
    return render_template('FaceDetectionProject.html')


@app.route('/DataStrcutureAndAlgorithm')
def project2_route():
    return render_template('DataStrcutureAndAlgorithm.html')


@app.route('/TwitterBot')
def project3_route():
    return render_template('TwitterBot.html')


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email}   |   {subject}   |   {message}')



@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_file(data)
        return render_template('thankyou.html')
    else:
        return 'Form not submitted, something wrong'





