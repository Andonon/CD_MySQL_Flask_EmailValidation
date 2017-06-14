import re
from mysqlconnection import MySQLConnector
from flask import Flask, render_template, redirect, request, flash
app = Flask(__name__)
mysql = MySQLConnector(app,'emailvalidation')

@app.route('/')
def index():
    return render_template('emailvalidation.html')

@app.route('/checkemail', methods=['POST'])
def checkemail():
    if request.method == 'POST':
        print "14 === Detected POST"
        print "15 === request form:", request.form
        email = request.form['email']
        print "17 === email: ", email
        if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
            print "19 re did NOT match, email is valid"
            flash = 'Invalid Email'
            print "21 flashed error for email invalid"
            return redirect('/')
        else:
            return redirect('/success')

@app.route('/success')
def successpage():
    query = "select email from users"
    usersemail = mysql.query_db(query)
    print usersemail
    return render_template('emailvalidationsuccess.html', usersemail=usersemail)

app.run(debug=True)