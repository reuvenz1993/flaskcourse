import requests
from trivia import app,db
from flask import render_template, redirect, request, url_for, flash,abort , session  , escape , make_response , jsonify
import json
from trivia.models import Score
from sqlalchemy import desc

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/submit_to_scoreboard', methods=['GET', 'POST'])
def submit_to_scoreboard():
    _name = request.form['name']
    _score = int ( request.form['score'] )
    print('hi')
    print('hi')
    new_score = Score( name = _name , score = _score)
    db.session.add(new_score)
    db.session.commit()
    #print (new_score)
    #scoreboard_res = Score.query.order_by(desc(Score.score)).all()
    #print (scoreboard_res)
    #scoreboard = [i.as_dict() for i in scoreboard_res]
    return get_scoreboard()

@app.route('/get_scoreboard', methods=['GET', 'POST'])
def get_scoreboard():
    scoreboard_res = Score.query.order_by(desc(Score.score)).all()
    scoreboard = [i.as_dict() for i in scoreboard_res]
    return jsonify(scoreboard)