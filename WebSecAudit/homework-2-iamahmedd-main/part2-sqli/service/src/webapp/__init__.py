from flask import Flask
from webapp.db import init_db, insert_db, run_script
from os import environ
from secrets import choice
from string import ascii_lowercase, digits, ascii_uppercase
def get_flag():
    flag = environ.get("CHALLENGE_FLAG", "{the_flag_is_undefined_?ax?d7e?fp?2?8?0}")
    final_flag = ""
    charset = digits + ascii_lowercase
    for c in flag:
        if c == "?": 
            final_flag += ''.join(choice(charset))
        else:
            final_flag += c
    return final_flag
flag_table_sql = """
CREATE TABLE {} (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  {} VARCHAR (100) NOT NULL
);
"""
def create_random_string(str_len=8):
    keyspace = ascii_lowercase + digits
    random_string = ""
    for _ in range(str_len):
        random_string += choice(keyspace)
    return random_string
def create_flag_table(app):
    run_script(app, flag_table_sql.format(app.flag_table, app.flag_column))
def insert_flag_into_db(app):
    with app.app_context():
        insert_db(
            app,
            f"INSERT INTO {app.flag_table} ({app.flag_column}) VALUES (?)",[app.flag])
        insert_db( app,"INSERT INTO log (username, action, user_agent) VALUES (?, ?, ?)", ['admin', 'register', app.flag])
def create_app():
    app = Flask(__name__)
    app.debug = False
    app.config['DB_PATH'] = ".sqldb"
    app.flag_table = "flag"
    app.flag_column = "flag"
    app.flag = get_flag()
    app.secret_key = create_random_string(32)
    init_db(app)
    create_flag_table(app)
    insert_flag_into_db(app)
    return app
app = create_app()
from webapp import views

