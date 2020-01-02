import requests
from trivia import app,db
from flask import render_template, redirect, request, url_for, flash,abort , session  , escape , make_response
import json
from trivia.models import Score


@app.route('/', methods=['GET', 'POST'])
def index_trivia():
    return render_template('index_trivia.html')

@app.route('/submit_to_scoreboard', methods=['GET', 'POST'])
def submit_to_scoreboard():
    _name = request.form['name']
    _score = int ( request.form['score'] )
    print('hi')
    print('hi')
    new_score = Score( name = _name , score = _score)
    db.session.add(new_score)
    db.session.commit()
    print (new_score)
    scoreboard = Score.query.all()
    print (scoreboard)
    return json.dumps(scoreboard)


#@app.route('/quest')
#def quest():
#    return requests.get('http://example.com').content

if __name__ == '__main__':
    app.run(debug=True)
