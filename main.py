import sqlite3

from flask import Flask, redirect, url_for, request, session
from flask_session import Session
from DBHandler import DBHandler

app = Flask(__name__)

SESSION_TYPE = 'filesystem'
app.config.from_object(__name__)
Session(app)

@app.route('/delete/')
def delete():
    dbh = DBHandler()
    dbh.clear_users()
    return 'deleted'

@app.route('/adduser/')
def success():
    dbHandler = DBHandler()
    username = request.args.get('username')
    nickname = request.args.get('nickname')
    dbHandler.insert_user(username, nickname)
    return {'username': username, 'nickname': nickname}

@app.route('/login', methods=['GET'])
def login():
    session
    username = request.args.get('username')
    db_handle = DBHandler()
    nickname = db_handle.get_nickname(username)
    return {'nickname': nickname}


if __name__ == '__main__':
    app.run(debug=True)