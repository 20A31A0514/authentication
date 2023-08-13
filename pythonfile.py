from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'


users = {
    'user1': 'password1',
    'user2': 'password2'
}

@app.route('/')
def index():
    if 'username' in session:
        return f'Welcome, {session["username"]}! <a href="/logout">Logout</a>'
    return 'Please <a href="/login">login</a> or <a href="/register">register</a>.'

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username not in users:
            users[username] = password
            return redirect(url_for('login'))
        return 'Username already exists.'

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('index'))

        return 'Invalid username or password.'
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
