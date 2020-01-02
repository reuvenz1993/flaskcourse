from trivia import db
from flask_login import UserMixin
# By inheriting the UserMixin we get access to a lot of built-in attributes
# which we will be able to call in our views!
# is_authenticated()
# is_active()
# is_anonymous()
# get_id()

class Score(db.Model, UserMixin):

    # Create a table in the db
    __tablename__ = 'Score'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64))
    score = db.Column(db.Integer)

    def __init__(self, name, score):
        self.name = name
        self.score = score

#def __repr__(self):
#	return '{} - {}'.format(self.name, self.score)

    def as_dict(self):
        return {'name': self.name , 'score': self.score }
