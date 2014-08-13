import pymongo
import os

from lib.singleton import Singleton

MONGO_URL = os.environ.get('MONGOLAB_URI')
 
@Singleton
class MongoDb:
  def connect(self):
    if MONGO_URL:
      # Get a connection
      conn = pymongo.Connection(MONGO_URL)
      # Get the database
      db = conn[urlparse(MONGO_URL).path[1:]]
    else:
      # Not on an app with the MongoHQ add-on, do some localhost action
      conn = pymongo.Connection()
      db = conn['testdb']

    return db

# collection = MongoDb.Instance.connect 
# # Test stuff
# collection.insert({"testdoc":"totaltest"})
# print db.test_collection.find()[0]