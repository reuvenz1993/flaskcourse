from loginproject import app,db
from flask import render_template, redirect, request, url_for, flash,abort
from flask_login import login_user,login_required,logout_user, current_user
from loginproject.models import User
from loginproject.forms import LoginForm, SignupForm


@app.route('/', methods=['GET', 'POST'])
def index():
    if current_user.is_authenticated:
        return redirect(url_for('main'))

    loginform = LoginForm()
    signupform = SignupForm()

    if loginform.validate_on_submit():
        the_user = User.query.filter_by(username = loginform.username.data).first()
        if the_user is not None and the_user.check_password(loginform.password.data)   :
            login_user(the_user, remember=True)
            print ('login scss')
            return redirect (url_for('main'))

    if signupform.validate_on_submit():
        new_user = User(email=signupform.email.data ,
                    username=signupform.username.data ,
                    password= signupform.password.data )
        db.session.add(new_user)
        db.session.commit()
        signupform.username.data = ""
        signupform.email.data = ""

    return render_template('index.html' , loginform = loginform , signupform = signupform )


@app.route('/trivia', methods=['GET', 'POST'])
@login_required
def trivia():
    return render_template('trivia.html')


@app.route('/main', methods=['GET', 'POST'])
@login_required
def main():
    return render_template('main.html')


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
