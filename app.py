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
    data = request.get_data()
    print  (data)
    name = data['name']
    score = data['score']
    new_score = Score( name = name , score = score)
    db.session.add(new_score)
    db.session.commit()
    print (new_score)
    return json.dumps(new_score)


#@app.route('/quest')
#def quest():
#    return requests.get('http://example.com').content

if __name__ == '__main__':
    app.run(debug=True)
