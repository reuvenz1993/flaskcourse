from flask import Flask, render_template, session, redirect, url_for, session, flash
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField,
                     RadioField,SelectField,TextField,
                     TextAreaField,SubmitField)
from wtforms.validators import DataRequired
import os
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
#__file__ = python file name


app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'mysecretkey'

db = SQLAlchemy(app)

class Puppy(db.Model):
    id = (db.Integer, primary)



class loginForm(FlaskForm):
    breed = StringField('What breed are you?' , validators=[DataRequired()] )
    neu = BooleanField("have you been new ?")
    mood = RadioField("what is the mood ?", choices=[('mood one', 'happy'),('mood two', 'great') , ('mood three', 'ok') , ('mood four', 'bad') ])
    food = SelectField (u'Pick your favorite food:' , choices=[('fish', 'fish'),('beef', 'beef') , ('corn', 'corn')  ] )
    feedback = TextAreaField()
    submit = SubmitField("Submit")
    
    
@app.route('/', methods=['GET', 'POST'])
def index():
    breed = False
    form = loginForm()
    
    if form.validate_on_submit():
        session['breed'] = form.breed.data
        session['neu'] = form.neu.data
        session['mood'] = form.mood.data
        session['food'] = form.food.data
        session['feedback'] = form.feedback.data
        return redirect (url_for('thankyou'))
    
    return render_template('index.html' , form = form )

@app.route('/thankyou', methods=['GET', 'POST'])
def thankyou():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)