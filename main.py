from flask import Flask, request, redirect, render_template


app = Flask(__name__)
app.config['DEBUG'] = True



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/", methods=['POST'])
def validate_form_values():
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify']
    email = request.form['email']

    username_error = ''
    password_error = ''
    email_error = ''

    verify_username_error = ''
    verify_password_error = ''
   

    if username == '' or len(username) > 20 or len(username) < 3:
        username_error = 'Please enter a valid username'
        username = ''
    else:
        username 
    
    if password == '' or len(password) > 20 or len(password) < 3:
        password_error = 'Please enter a valid password'
        password = ''
    else:
        password 

    if verify_password == '' or verify_password != password:
        verify_password_error = 'Please enter a valid password'
        verify_password = ''
    else:
        verify_password

    if email == '' or len(email) > 20 or len(email) < 3 or '@' not in email or '.' not in email:
        email_error = 'Please enter a valid email address'
        email = ''
    else:
        email

    if not username_error and not password_error and not verify_password_error:
        return redirect('/welcome?username={}'.format(username))
    else:
        return render_template('index.html', password_error = password_error, verify_password_error = verify_password_error, username_error = username_error, email_error = email_error)

@app.route('/welcome')
def welcome():
    username = request.args.get('username')
    return render_template('welcome.html', username = username)

app.run()
