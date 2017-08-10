from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = 'secret'
mysql = MySQLConnector(app,'email_validation')

@app.route('/')
def index():


	return render_template('index.html')

@app.route('/process', methods=['POST'])
def create():
	if len(request.form['email']) < 1:
		flash("Name cannot be empty!")
	elif not EMAIL_REGEX.match(request.form['email']):
		flash("Invalid Email Address!")
	else:
		flash("Success!")
		query = "INSERT INTO email (email, created_at) VALUES (:email, NOW())"

		data = {
         	'email': request.form['email'],

       	}

		mysql.query_db(query, data)
	return redirect('/')






app.run(debug=True)

