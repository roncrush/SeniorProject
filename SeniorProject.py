from flask import Flask, render_template, request, session, redirect, url_for
from flask.ext.bcrypt import Bcrypt
import utilities
import amm_db

app = Flask(__name__)
app.debug = True

# pushed random letters, numbers, symbols: can be changed
# Used for session
app.secret_key = 'F847Jsa8sa&320-1=-!@('

bcrypt = Bcrypt(app)

db = amm_db.AmmDB()


@app.route('/', methods=['GET', 'POST'])
def main_page():
    session['userID'] = None

    if request.method == 'POST':
        if request.form.get('email', None) is not None:
            db.add_user(fn=request.form['first_name'], ln=request.form['last_name'], email=request.form['email'],
                        uname=request.form['username'], passwd=bcrypt.generate_password_hash(request.form['password']))
        elif request.form.get('username-login', None) is not None:
            data = db.get_user(uname=request.form['username-login'], exact=True)

            if len(data) > 0:
                if bcrypt.check_password_hash(data[0]['passwd'], request.form['password-login']):
                    user_id = data[0]['id']
                    session['user_id'] = user_id
                    return redirect(url_for('home'))

                else:
                    return render_template('MainPage.html', error='Username/Password is incorrect')
            else:
                return render_template('MainPage.html', error='Username/Password is incorrect')

    return render_template('MainPage.html')


@app.route('/home')
def home():
    if session.get('user_id', None) is None:
        return redirect(url_for('main_page'))
    else:
        user_info = db.get_user(session.get('user_id'))
        return render_template('home.html', user=user_info)


@app.route('/profile', methods=['POST', 'GET'])
def profile():
    if session.get('user_id', None) is None:
        return redirect(url_for('main_page'))
    else:
        user_info = db.get_user(session.get('user_id'))
        if request.method == 'POST':
            response = 'Passwords do not match!'
            if request.form['password'] != request.form['c_password']:
                return render_template('profile.html', user=user_info, response=response, css_class='red-text')
            else:
                if request.form['password'] != '':
                    db.edit_user(session.get('user_id'), email=request.form['u_email'],
                             fname=request.form['fname'], lname=request.form['lname'],
                             passwd=bcrypt.generate_password_hash(request.form['password']),
                                 phone = request.form['phone'])
                else:
                    db.edit_user(session.get('user_id'), email=request.form['u_email'],
                             fname=request.form['fname'], lname=request.form['lname'],
                             passwd='', phone=request.form['phone'])

                response = 'Updates made to profile!'
                user_info = db.get_user(session.get('user_id'))

                return render_template('profile.html', response=response, css_class='green-text', user=user_info)
        else:
            return render_template('profile.html', user=user_info)


@app.route('/create_event', methods=['POST', 'GET'])
def create_event():
    if session.get('user_id', None) is None:
        return redirect(url_for('main_page'))
    user_info = db.get_user(session.get('user_id'))
    return render_template('create_event.html', user=user_info)


@app.route('/calendar')
def calendar():
    if session.get('user_id', None) is None:
        return redirect(url_for('main_page'))
    user_info = db.get_user(session.get('user_id'))
    return render_template('SearchResultsPage.html', user=user_info)


@app.route('/rosters')
def rosters():
    if session.get('user_id', None) is None:
        return redirect(url_for('main_page'))
    user_info = db.get_user(session.get('user_id'))
    return render_template('RostersPage.html', user=user_info)


@app.route('/logout')
def logout():
    if session.get('user_id', None) is None:
        return redirect(url_for('main_page'))
    session.clear()
    return main_page()


if __name__ == '__main__':
    app.run()
