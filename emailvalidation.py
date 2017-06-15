import re
from mysqlconnection import MySQLConnector
from flask import Flask, render_template, redirect, request, flash, session
#pylint: disable=C0103,C0111
app = Flask(__name__)
mysql = MySQLConnector(app, 'emailvalidation')
app.secret_key = 'lkjas09a8sd098998asdsdlasdlkjasd9089'

@app.route('/')
def index():
    return render_template('emailvalidation.html')

@app.route('/checkemail', methods=['POST'])
def checkemail():
    if request.method == 'POST':
        session['email'] = request.form['email']
        if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", session['email']):
            flash("Invalid Email Address. Please try again.")
        else:
            query = "INSERT INTO emails (email, created_at, updated_at) values (:email, now(), now())"
            data = {
                'email': session['email']
            }
            mysql.query_db(query, data)
            return redirect('/success')
    return redirect('/')
@app.route('/success')
def successpage():
    query = "select id, email, concat(Month(created_at),'/',Day(created_at),'/',Year(created_at),' ',Time(created_at)) as Date from emails"
    emails = mysql.query_db(query)
    print emails
    return render_template('emailvalidationsuccess.html', all_emails=emails)

app.run(debug=True)