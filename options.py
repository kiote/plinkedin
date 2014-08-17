from tornado.options import define

# options
define("port", default=5000, help="run on the given port", type=int)
define("state", default="abcd", help="Used to prevent CSRF", type=str)
define("redirect_url", default="http://protected-waters-8043.herokuapp.com/", \
  help="OAuth2 redirect URL", type=str)
define("client_id", default="wrong", help="Value of API key", type=str)
define("linkedin_oauth", default="wrong", help="LinkedIn OAuth URL", type=str)
define("code", default="wrong", type=str)