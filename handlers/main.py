import tornado.web
from models.mongo import MongoDb


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        collection = MongoDb.Instance().connect()
        # Test stuff
        collection.users.insert({"id": 1, "code": self.get_argument('code')})
        users=collection.users
        self.render(
          "main.html",
          page_title='Heroku Funtimes',
          page_heading=users.find_one({"id": 1})["code"]
        )