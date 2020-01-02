#import requests
from trivia import app,db
#from flask import render_template, redirect, request, url_for, flash,abort , session  , escape , make_response , jsonify
#import json
#from trivia.models import Score
#from sqlalchemy import desc

import trivia.views

if __name__ == '__main__':
    app.run(debug=True)
