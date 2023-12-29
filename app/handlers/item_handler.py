import json
from tornado.web import RequestHandler
from app.services.item_service import ItemService

class ItemHandler(RequestHandler):
    service = ItemService()

    def get(self, key):
        item = self.service.get_item(key)
        if item:
            self.write(item)
        else:
            self.set_status(404)
            self.write({"error": "Item not found"})

    def post(self, key):
        try:
            data = json.loads(self.request.body)
            self.service.add_item(key, data)
            self.write({"message": "Item added successfully"})
        except json.JSONDecodeError:
            self.set_status(400)
            self.write({"error": "Invalid JSON"})

    def put(self, key):
        try:
            data = json.loads(self.request.body)
            if self.service.update_item(key, data):
                self.write({"message": "Item updated successfully"})
            else:
                self.set_status(404)
                self.write({"error": "Item not found"})
        except json.JSONDecodeError:
            self.set_status(400)
            self.write({"error": "Invalid JSON"})

    def delete(self, key):
        if self.service.delete_item(key):
            self.write({"message": "Item deleted successfully"})
        else:
            self.set_status(404)
            self.write({"error": "Item not found"})

    def patch(self, key):
        try:
            data = json.loads(self.request.body)
            if self.service.patch_item(key, data):
                self.write({"message": "Item updated successfully"})
            else:
                self.set_status(404)
                self.write({"error": "Item not found"})
        except json.JSONDecodeError:
            self.set_status(400)
            self.write({"error": "Invalid JSON"})
