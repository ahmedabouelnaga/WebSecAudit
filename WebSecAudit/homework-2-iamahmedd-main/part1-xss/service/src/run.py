#!/usr/bin/python3
from webapp import app
from gunicorn.app.base import BaseApplication
class GunicornApp(BaseApplication):
    #https://github.com/rragundez/app-skeleton/blob/f35adda20c415df10348af61d6ea8dfa4277c520/app/resources/gunicorn_app.py#L4
    def __init__(self, flask_app, settings=None):
        self.flask_app = flask_app
        self.settings = settings or {}
        super().__init__()

    def load_config(self):
        for k, v in self.settings.items():
            self.cfg.set(k, v)

    def load(self):
        return self.flask_app

GunicornApp(app,{'bind': "0.0.0.0:8000"}).run()