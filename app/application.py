from tornado.web import Application
from app.routes import routes

def make_app():
    return Application(routes)
