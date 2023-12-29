from app.handlers.main_handler import MainHandler
from app.handlers.item_handler import ItemHandler

routes = [
    (r"/", MainHandler),
    (r"/item/([^/]+)", ItemHandler),
]
