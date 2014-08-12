import tornado.web

class MainHandler(tornado.web.RequestHandler):
  def get(self):
    self.render(
      "main.html",
      page_title='Heroku Funtimes',
      page_heading=self.get_argument('code')
    )