import tornado.ioloop
import tornado.web
import logging
import sys

from tornado.gen import coroutine
from tornado.httpclient import AsyncHTTPClient, HTTPRequest, HTTPError

logging.warning('tornado')

class MainHandler(tornado.web.RequestHandler):
  def initialize(self):
    self.client = AsyncHTTPClient()

  @coroutine
  def get(self):
    yield self.handle()

  @coroutine
  def handle(self):
    logging.warning(self.request.method)

    request = HTTPRequest(
        url='http://yandex.ru',
        method=self.request.method
    )
    
    try:
      response = yield self.client.fetch(request)
      logging.warning(response)
    finally:
      self.write("response")
      self.finish() 

application = tornado.web.Application([
  (r"/", MainHandler),
])

if __name__ == "__main__":
  application.listen(5000)
  tornado.ioloop.IOLoop.instance().start()