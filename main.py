#!/usr/bin/env python
import os.path
import tornado.escape
import tornado.httpserver
import tornado.ioloop
import tornado.web

from handlers.auth import AuthHandler
from handlers.main import MainHandler

# import and define tornado-y things
from tornado.options import options

import options

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

def main():
  tornado.options.parse_command_line()
  tornado.options.parse_config_file("config.cnf")

  http_server = tornado.httpserver.HTTPServer(Application())
  http_server.listen(tornado.options.options.port)

  tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
  main()
