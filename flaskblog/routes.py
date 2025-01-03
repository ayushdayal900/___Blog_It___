from flask import render_template, flash, redirect, url_for, request
from flaskblog.models import User, Post
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm
from flask_login import login_user, current_user, logout_user, login_required


posts = [
    {
        'author':'Ayush Dayal',
        'title':'Blog 1',
        'content':'This is the first blog',
        'date_posted':'06-10-2004'
    },
{
        'author':'Aditya Dayal',
        'title':'Blog 2',
        'content':'This is the second blog',
        'date_posted':'08-09-2002'
    },
{
        'author':'Padmaja Dayal',
        'title':'Blog 3',
        'content':'This is the third blog',
        'date_posted':'17-01-2010'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts = posts, title = "Ayush's Blogs")

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/register', methods=['GET','POST'] )
def register():
    # ----------------------------------------- break -----------------------------
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f"Your account has been created..! You are now able to log in", 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title = 'Register', form=form)

@app.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check email and password.', 'danger')
    return render_template('login.html', title = 'Login', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/account')
@login_required
def account():
    return render_template('account.html', title='Account')
