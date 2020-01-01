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
    score = Score( name=POST['name'] , )
    db.session.add(score)
    db.session.commit()
    return json.dumps("test")


#@app.route('/quest')
#def quest():
#    return requests.get('http://example.com').content

if __name__ == '__main__':
    app.run(debug=True)
