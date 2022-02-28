# You can add to this file in the editor.
import pyotp # generrates one time passwords
import sqlite3 # database for username and password
import hashlib # secure hases and message digests
import uuid # for creating unique identifiers
from flask import Flask, request

app = Flask(__name__) # create the Flask app

db_name = 'test.db' # name of the database

@app.route('/') # the root of the site
def index():
    return 'Welcome to hands on lab for the evolution of passwords systems!'


######## Plain text password #########
@app.route('/signup/v1', methods=["POST"]) # the root of the site
def signup_v1():
    conn = sqlite3.connect(db_name) # connect to the database
    c = conn.cursor() # create a cursor object
    c.execute('''CREATE TABLE IF NOT EXISTS USER_PLAIN (USERNAME TEXT PRIMARY KEY NOT NULL, PASSWORD TEXT NOT NULL)''') # create the table
    conn.commit() # commit the changes
    try:
        c.execute("INSERT INTO USER_PLAIN (USERNAME,PASSWORD)" "VALUES ('{0}', '{1}')".format(request.form['username'], request.form['password']))
        conn.commit()
    except sqlite3.IntegrityError:
        return "Username has been registered"
    print("username: ", request.form['username'], "password: ", request.form['password'])
    return "Sign up successful"

def verify_plain(username, password):
    conn = sqlite3.connect(db_name) # connect to the database
    c = conn.cursor() # create a cursor object
    query = "SELECT PASSWORD FROM USER_PLAIN WHERE USERNAME = '{0}'".format(username)
    c.execute(query)
    records = c.fetchone()
    conn.close
    if not records:
        return False
    return records[0] == password

@app.route('/login/v1', methods=["GET", "POST"]) # the root of the site
def login_V1():
    error = None
    if request.method == "POST":
        if verify_plain(request.form['username'], request.form['password']):
            return "Login successful"
        else:
            return "Login failed"
    else:
        #return render_template('login.html', error=error)
        error = "Invalid Method"
    return error

@app.route('/signup/v2', methods=["GET", "POST"]) # the root of the site
def signup_v2():
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS USER_HASH (USERNAME TEXT PRIMARY KEY NOT NULL, HASH TEXT NOT NULL)''')
    conn.commit()
    try:
        hash_value = hashlib.sha256(request.form['password'].encode()).hexdigest()
        c.execute("INSERT INTO USER_HASH (USERNAME, HASH)" "VALUES ('{0}', '{1}')".format(request.form['username'], hash_value))
        conn.commit()
    except sqlite3.IntegrityError:
        return "Username has been registered"
    print("username: ", request.form['username'], "password: ", request.form['password'], 'hash: ', hash_value)
    return "Sign up successful"

def verify_hash(username, password):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    query = "SELECT HASH FROM USER_HASH WHERE USERNAME = '{0}'".format(username)
    c.execute(query)
    records = c.fetchone()
    conn.close
    if not records:
        return False
    return records[0] == hashlib.sha256(password.encode()).hexdigest()

@app.route('/login/v2', methods=["GET", "POST"]) # the root of the site
def login_V2():
    error = None
    if request.method == "POST":
        if verify_hash(request.form['username'], request.form['password']):
            error = "Login successful"      
        else:
            error = "Login failed"
    else:
        #return render_template('login.html', error=error)
        error = "Invalid Method"
    return error

# create local webserver on port 5000 with self-signed certificate
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, ssl_context='adhoc')

