from app import app
from flask import Flask, redirect, url_for, session, request, render_template
from flask_oauthlib.client import OAuth, OAuthException
import datetime
import requests
import json


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
