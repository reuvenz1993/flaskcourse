from flask import Flask, render_template, session, redirect, url_for, session, flash
from forms import AddForm, DeleteForm , AddForm
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))
#__file__ = python file name


app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'mysecretkey'

db = SQLAlchemy(app)
Migrate(app,db)

class Puppy(db.Model):

    __tablename__ = 'puppies'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.Text)
    # This is a one-to-many relationship
    # A puppy can have many toys
    toys = db.relationship('Toy',backref='puppy',lazy='dynamic')
    # This is a one-to-one relationship
    # A puppy only has one owner, thus uselist is False.
    # Strong assumption of 1 dog per 1 owner and vice versa.
    owner = db.relationship('Owner',backref='puppy',uselist=False)

    def __init__(self,name):
        # Note how a puppy only needs to be initalized with a name!
        self.name = name


    def __repr__(self):
        if self.owner:
            return f"Puppy id is {self.id} Puppy name is {self.name} and owner is {self.owner.name}"
        else:
            return f"Puppy id is {self.id} Puppy name is {self.name} and has no owner assigned yet."

    def report_toys(self):
        print("Here are my toys!")
        for toy in self.toys:
            print(toy.item_name)


class Toy(db.Model):

    __tablename__ = 'toys'

    id = db.Column(db.Integer,primary_key = True)
    item_name = db.Column(db.Text)
    # Connect the toy to the puppy that owns it.
    # We use puppies.id because __tablename__='puppies'
    puppy_id = db.Column(db.Integer,db.ForeignKey('puppies.id'))

    def __init__(self,item_name,puppy_id):
        self.item_name = item_name
        self.puppy_id = puppy_id


class Owner(db.Model):

    __tablename__ = 'owners'

    id = db.Column(db.Integer,primary_key= True)
    name = db.Column(db.Text)
    # We use puppies.id because __tablename__='puppies'
    puppy_id = db.Column(db.Integer,db.ForeignKey('puppies.id'))

    def __init__(self,name,puppy_id):
        self.name = name
        self.puppy_id = puppy_id




    
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html' , form = form )


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = AddForm()
    if form.validate_on_submit():
        new_pup = Puppy(form.name.data)
        db.session.add(new_pup)
        db.session.commit()
        form.name.data=""
        return redirect(url_for('list'))
    return render_template('add.html' , form = form)

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    form = DeleteForm()

    if form.validate_on_submit():
        print ("del on submit")
        id = form.id.data
        pup = Puppy.query.get(id)
        db.session.delete(pup)
        db.session.commit()
        return redirect(url_for('list'))

    return render_template('delete.html' , form = form )

@app.route('/list', methods=['GET', 'POST'])
def list():
    pup_list = Puppy.query.all()
    return render_template('list.html' , pup_list = pup_list )

@app.route('/add_owner', methods=['GET', 'POST'])
def add_owner():
    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data
        puppy_id = form.puppy_id.data
        new_owner = Owner( name , puppy_id )
        print (new_owner)
        db.session.add(new_owner)
        db.session.commit()
        return redirect(url_for('list'))
    return render_template('add_owner.html' , form = form )

if __name__ == '__main__':
    app.run(debug=True)