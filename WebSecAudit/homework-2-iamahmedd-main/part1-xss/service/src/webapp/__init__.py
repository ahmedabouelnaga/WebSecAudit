from flask import Flask


def create_app():
  app = Flask(__name__)
  app.debug = True
  return app
app = create_app()

from webapp import views

