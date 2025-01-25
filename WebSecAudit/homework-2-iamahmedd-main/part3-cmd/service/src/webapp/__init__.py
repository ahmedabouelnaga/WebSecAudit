from flask import Flask
from os import environ
from secrets import choice
from string import ascii_lowercase, digits, ascii_uppercase

def get_flag():
  flag = environ.get("CHALLENGE_FLAG","{the_flag_is_undefined_?ax?d7e?fp?2?8?0}")
  final_flag = ""
  charset = digits + ascii_lowercase
  for c in flag:
    if c == "?": 
      final_flag += str(''.join(choice(charset)))
    else:
      final_flag += c
  return final_flag

def create_random_string(str_len=8):
  keyspace = ascii_lowercase + digits
  random_string = ""
  for c in range(str_len):
    random_string += choice(keyspace)
  return random_string


def create_app():
  app = Flask(__name__)
  app.debug = True
  app.flag = get_flag()
  with open("/tmp/flag.txt", "w") as f:
    f.write(app.flag)
  return app
app = create_app()

from webapp import views

