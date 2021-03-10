import time
from flask import Flask, request
from flask.json import jsonify
import random
from api import news

app = Flask(__name__)

@app.route('/search')
def search_by_title():
    """
    Seach for news articles across Zimbabwean online news websites
    """
    # search agent
    agent = news.NewsAgent()

    if 'category' in  request.args: 
        return jsonify(agent.search_by_category(request.args['category']))
   
    elif 'title' in  request.args: 
        return jsonify(agent.search_by_title(request.args['title']))
    else:
        return []
