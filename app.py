from flask import Flask, request, render_template, session, redirect, url_for
from translation import maay, rev_maay

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for using sessions

USER_CREDENTIALS = {'username': 'admin', 'password': 'password'}

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == USER_CREDENTIALS['username'] and password == USER_CREDENTIALS['password']:
            session['logged_in'] = True
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error="Invalid credentials")

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

@app.route('/', methods=['GET', 'POST'])
def index():
    # Clear session and redirect to login if not logged in
    if not session.get('logged_in'):
        session.clear()  # Clear session to ensure no residual data
        return redirect(url_for('login'))

    if request.method == 'POST':
        user_input = request.form.get('user_input', '').strip().lower()
        selected_function = request.form.get('action')

        if selected_function == 'Function 1':
            session['result'] = maay(user_input)
        elif selected_function == 'Function 2':
            session['result'] = rev_maay(user_input)
        else:
            session['result'] = None

        return redirect(url_for('index'))

    result = session.pop('result', None)
    return render_template('index.html', result=result)

""" if __name__ == '__main__':
    app.run(debug=True) """