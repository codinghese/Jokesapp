from flask import Flask,render_template,request,redirect, url_for,flash, abort, session
import json
import requests
import os.path
from werkzeug.utils import secure_filename
app= Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')
@app.route('/mainfun')
def mainfun():
	r=requests.get('https://official-joke-api.appspot.com/jokes/random')
	response=r.json()
	j1=response['setup']
	j2=response['punchline']
	joke=[j1,j2]
	return render_template('jokes.html',jokes=joke)