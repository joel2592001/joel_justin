from flask import Flask, request, render_template, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'secretkey'  # replace with your own secret key


def zero(op=None):
    if op is None:
        return 0
    else:
        return op(0)


def one(op=None):
    if op is None:
        return 1
    else:
        return op(1)


def two(op=None):
    if op is None:
        return 2
    else:
        return op(2)


def three(op=None):
    if op is None:
        return 3
    else:
        return op(3)


def four(op=None):
    if op is None:
        return 4
    else:
        return op(4)


def five(op=None):
    if op is None:
        return 5
    else:
        return op(5)


def six(op=None):
    if op is None:
        return 6
    else:
        return op(6)


def seven(op=None):
    if op is None:
        return 7
    else:
        return op(7)


def eight(op=None):
    if op is None:
        return 8
    else:
        return op(8)


def nine(op=None):
    if op is None:
        return 9
    else:
        return op(9)


def plus(y):
    return lambda x: x + y


def minus(y):
    return lambda x: x - y


def times(y):
    return lambda x: x * y


def divided_by(y):
    return lambda x: x // y


users = {
    'master': {
        'password': 'masterpass',
        'role': 'master'
    }
}

activities = []


def evaluate(expression):
    """Evaluates the given expression and returns the result."""
    try:
        return eval(expression)
    except (SyntaxError, NameError):
        return 'Invalid Expression'


@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username]['password'] == password:
            session['username'] = username
            session['role'] = users[username]['role']
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error='Invalid username or password')
    else:
        return render_template('login.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        role = request.form['role']
        if username in users:
            return render_template('signup.html', error='Username already taken')
        else:
            users[username] = {
                'password': password,
                'role': role
            }
            session['username'] = username
            session['role'] = role
            return redirect(url_for('login'))
    else:
        return render_template('signup.html')


@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))
    elif session['role'] == 'student':
        return render_template('dashboard_student.html', activities=activities)
    else:
        return render_template('dashboard_master.html', activities=activities, evaluate=evaluate)


@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('role', None)
    return redirect(url_for('home'))


@app.route('/request_input', methods=['POST'])
def request_input():
    if session['role'] == 'master':
        activity = request.form['activity']
        activities.append(activity)
        return redirect(url_for('dashboard'))
    else:
        return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
