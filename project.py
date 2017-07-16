from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from sqlalchemy import create_engine, asc,desc
from sqlalchemy.orm import sessionmaker

from flask import session as login_session
import random
import string
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests
from pprint import pprint
from functools import wraps
import pymysql.cursors
import urllib2
import requests

from requests.auth import HTTPBasicAuth


app = Flask(__name__)


@app.route('/')
def routeToMain():
    """ Main Page """
    return redirect(url_for('getMainPage'))



@app.route('/catalog', methods=['GET', 'POST'])         
def getMainPage():


    pprint (r.json())
    return "r.json()"




if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
    
