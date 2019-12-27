from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired

class AddForm(FlaskForm):
    name = StringField('What is the Puppy name ? : ' , validators=[DataRequired()] )
    submit = SubmitField("Submit")

class DeleteForm(FlaskForm):
    id = IntegerField('What is the Puppy id ? : ')
    submit = SubmitField("Submit")

class AddForm(FlaskForm):
    name = StringField('What is the owner name ? : ' , validators=[DataRequired()] )
    puppy_id = IntegerField('What is the Puppy id ? : ')
    submit = SubmitField("Submit")

