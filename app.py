from loginproject import app,db
from flask import render_template, redirect, request, url_for, flash,abort
from flask_login import login_user,login_required,logout_user
from loginproject.models import User
from loginproject.forms import LoginForm, SignupForm


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/welcome_user', methods=['GET', 'POST'])
@login_required
def welcome_user():
    return render_template('welcome_user.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()

        if user.check_password(form.password.data) and user is not None :
            login_user(user)
            flash('Logged in scss')

            next = request.args.get('next')

            if next == None or not next[0]=='/' :
                next = url_for('welcome_user')

            return redirect(next)

    return render_template('login.html' , form = form )

@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect (url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = SignupForm()
    if form.validate_on_submit():
        user = User(email=form.email.data ,
                    username=form.username.data ,
                    password= form.password.data )
        db.session.add(user)
        db.session.commit()
        flash('Thank for registration')
    return render_template('register.html' , form = form)

if __name__ == '__main__':
    app.run(debug=True)
