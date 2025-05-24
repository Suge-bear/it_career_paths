# app.py
from flask import Flask, render_template, redirect, url_for, request, session
from flask import render_template
from forms import LoginForm  # import your form
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFProtect
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from extensions import db  # ✅ From new extensions file

class SignUpForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Create Account')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db.init_app(app)

# Import models after db.init_app to avoid circular import
from models import User, CareerPath

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        username = form.username.data
        password = generate_password_hash(form.password.data)
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('signup.html', form=form)

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    paths = CareerPath.query.all()
    return render_template('dashboard.html', paths=paths)

@app.route('/career/<int:path_id>')
def career_detail(path_id):
    path = CareerPath.query.get_or_404(path_id)
    return render_template('career_path.html', path=path)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create tables if they don’t exist
    app.run(debug=True)
