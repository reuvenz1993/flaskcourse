import requests
from trivia import app,db
from flask import render_template, redirect, request, url_for, flash,abort


@app.route('/', methods=['GET', 'POST'])
def index_trivia():
    return render_template('index_trivia.html')


#@app.route('/quest')
#def quest():
#    return requests.get('http://example.com').content

if __name__ == '__main__':
    app.run(debug=True)
