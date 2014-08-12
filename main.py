#!/usr/bin/env python
import os.path
import tornado.escape
import tornado.httpserver
import tornado.ioloop
import tornado.web

# import and define tornado-y things
from tornado.options import define, options

define("port", default=5000, help="run on the given port", type=int)
define("state", default="abcd", help="Used to prevent CSRF", type=str)
define("redirect_url", default="http://protected-waters-8043.herokuapp.com/", \
  help="OAuth2 redirect URL", type=str)
define("client_id", default="wrong", help="Value of API key", type=str)
define("linkedin_oauth", default="wrong", help="LinkedIn OAuth URL", type=str)

import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class Application(tornado.web.Application):
  def __init__(self):
    handlers = [
      (r"/", MainHandler),
      (r"/auth", AuthHandler)
    ]
    settings = dict(
      template_path=os.path.join(os.path.dirname(__file__), "templates"),
      static_path=os.path.join(os.path.dirname(__file__), "static"),
      debug=True,
    )
    tornado.web.Application.__init__(self, handlers, **settings)

class MainHandler(tornado.web.RequestHandler):
  def get(self):
    self.render(
      "main.html",
      page_title='Heroku Funtimes',
      page_heading='Hi!'
    )

class AuthHandler(tornado.web.RequestHandler):
  def get(self):
    self.redirect( tornado.options.options.linkedin_oauth % (tornado.options.options.client_id, \
      tornado.options.options.state, tornado.options.options.redirect_url))

def main():
  tornado.options.parse_command_line()
  tornado.options.parse_config_file("config.cnf")

  http_server = tornado.httpserver.HTTPServer(Application())
  http_server.listen(tornado.options.options.port)
  # logging.warn(tornado.options.options.state)
  # start it up
  tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
  main()
