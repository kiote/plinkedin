import tornado.web

class AuthHandler(tornado.web.RequestHandler):
  def get(self):
    self.redirect( tornado.options.options.linkedin_oauth % (tornado.options.options.client_id, \
      tornado.options.options.state, tornado.options.options.redirect_url))