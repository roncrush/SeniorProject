from flask import Flask, render_template
import utilities

app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('MainPage.html')


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/profile')
def profile():
    return render_template('profile.html')


@app.route('/create_event')
def create_event():
    return render_template('create_event.html', key=utilities.get_maps_key())


if __name__ == '__main__':
    app.run()
