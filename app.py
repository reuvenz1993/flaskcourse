from flask import Flask, render_template, session, redirect, url_for, session, flash
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField,
                     RadioField,SelectField,TextField,
                     TextAreaField,SubmitField)
from wtforms.validators import DataRequired

print ("hi")

app=Flask(__name__)


app.config['SECRET_KEY'] = 'mysecretkey'

class loginForm(FlaskForm):
    username = StringField('enter username')
    password = StringField('enter password')
    email = StringField('enter password')
    submit = SubmitField(label="click to submit")
    
    
@app.route('/', methods=['GET', 'POST'])
def index():
    username = False
    form = loginForm()
    
    if form.validate_on_submit():
        session['username'] = form.username.data
        flash(f"You just changed your username to: {session['username']}")
        return redirect(url_for("index"))
    
    return render_template('index.html' , form = form , username = username )


if __name__ == '__main__':
    app.run(debug=True)