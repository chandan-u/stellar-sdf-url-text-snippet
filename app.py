from flask import Flask
from contextlib import closing
from flask import request
from flask import Response
import datetime
import flask
from flask import json, jsonify

import sqlite3

app = Flask(__name__)

DATABASE = './database.db'

def connect_db():
    return sqlite3.connect(DATABASE)

@app.cli.command('initdb')
def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('./schema.sql') as f:
            db.cursor().executescript(f.read())
        db.commit()


def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/")
def index():
    return "use this app to create text snippets and store them. \
            Access them later with URL until they are expired"




@app.route('/snippets', methods=['POST'])
def create_snippet():

    # TODO: else condition if request is not POST throw error
    if request.method == 'POST':
        print(request)
        data = request.json
        name = data['name']
        expires_in = data['expires_in']
        snippet = data['snippet']

        expires_at = datetime.datetime.now() + datetime.timedelta(seconds=expires_in)

        response = {
            'url': flask.url_for("index", _external=True) + 'snippets/' + name,
            'name': name,
            'expires_at': expires_at.__str__(),
            'snippet': snippet
        }

        # store in database
        con = get_db_connection()
        try:
            c =  con.cursor() # cursor
            # insert data
            c.execute("INSERT INTO snippets (snippetName, snippetExpTime, snippet) VALUES (?,?,?)", 
                (name, expires_at, snippet))
            con.commit() # apply changes
            # go to thanks page
            return Response(json.dumps(response), status=201, mimetype='application/json')
        except con.Error as err: # if error
            # then display the error in 'database_error.html' page
            return render_template('database_error.html', error=err)
        finally:
            con.close() 

        return 
    

@app.route('/snippets/<name>', methods=['GET'])
def get_snippet(name):
    

    con = get_db_connection()
    try:
        data = con.execute("SELECT snippetName, snippetExpTime, snippet FROM snippets where snippetName='{0}'".format(name)).fetchone()
        

        if data['snippetExpTime'] <= datetime.datetime.now().__str__():                 # TODO:bad idea to  compare strings though its valid for same formats

            response = {
                'url': flask.url_for("index", _external=True) + 'snippets/' + name,
                'name': name,
                'expires_at': data["snippetExpTime"].__str__(),
                'snippet': data["snippet"]
            }
         
            return Response(json.dumps(response), status=200, mimetype='application/json')
        else:
            return Response("'status':'404 not found'", status=404, mimetype='application/json')

    except con.Error as err: # if error
            # then display the error in 'database_error.html' page
            return render_template('database_error.html', error=err)                  # TODO: need to create database_error.html

    finally: 
        con.close()

    return


