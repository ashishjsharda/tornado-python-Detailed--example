from tornado.web import RequestHandler

class MainHandler(RequestHandler):
    def get(self):
        self.write("Welcome to the Tornado App!")
