import tornado.web
from models.mongo import MongoDb

class MainHandler(tornado.web.RequestHandler):
  def get(self):
    collection = MongoDb.Instance().connect()
    # Test stuff
    collection.insert({"testdoc":"totaltest"})
    self.render(
      "main.html",
      page_title='Heroku Funtimes',
      page_heading=self.get_argument('code')
    )