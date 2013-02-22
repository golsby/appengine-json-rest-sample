import packages # required for AppEngine to find third-party packages.
from google.appengine.ext import db
import datetime

from appengine_json_rest.appengine_json_rest import create_application


class Fruit(db.Model):
    name = db.StringProperty()
    width = db.IntegerProperty()
    created_datetime = db.DateTimeProperty(required=True, auto_now_add=True)
    modified_datetime = db.DateTimeProperty(required=True, auto_now=True, auto_now_add=True)
    created_date = db.DateProperty(required=True, auto_now_add=True)
    modified_date = db.DateProperty(required=True, auto_now=True, auto_now_add=True)
    created_time = db.TimeProperty(required=True, auto_now_add=True)
    modified_time = db.TimeProperty(required=True, auto_now=True, auto_now_add=True)
    rating = db.RatingProperty()
    location = db.GeoPtProperty()
    aliases = db.StringListProperty()
    destinations = db.ListProperty(db.GeoPt)
    touched_dates = db.ListProperty(datetime.datetime)


simple = create_application('simple', models = [Fruit])