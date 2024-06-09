from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    #Example before the db
    if username == 'admin' and password == 'admin':
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('index'))


@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        fn = request.form['fn']
        ln = request.form['ln']
        username = request.form['username']
        password = request.form['password']
        return redirect(url_for('index'))
    return render_template('register.html')

@app.route('/success')
def success():
    return "Login successful!"

@app.route('/admin')
def admin():
    balance = '∞'
    username = 'Admin'
    return render_template('admin.html', balance=balance, username=username)  #Balance



app.run(debug=True, port=5001)

