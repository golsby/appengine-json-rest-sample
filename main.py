import packages # required for AppEngine to find third-party packages.
from google.appengine.ext import db
import datetime
import base64

from appengine_json_rest.appengine_json_rest.application import JSONApplication
from appengine_json_rest.appengine_json_rest.errors import ForbiddenError, AuthenticationRequiredError


class Basket(db.Model):
    """
    A basket to store fruit in.
    """
    location = db.GeoPtProperty()

class Fruit(db.Model):
    basket = db.ReferenceProperty(Basket)
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


simple = JSONApplication('simple', models=[Fruit, Basket])

def basic_auth(request):
    authorized = {
        'naive': 'pa$sw0rd'
    }

    auth_header = request.headers.get("Authorization")

    if not auth_header:
        raise AuthenticationRequiredError({"WWW-Authenticate": 'Basic realm="{0}"'.format(request.host)})

    if not auth_header.startswith('Basic '):
        raise AuthenticationRequiredError({"WWW-Authenticate": 'Basic realm="{0}"'.format(request.host)})

    try:
        decoded = base64.b64decode(auth_header[6:])
        (user, pwd) = decoded.split(':')
        if authorized.get(user) != pwd:
            raise ForbiddenError()
    except:
        raise ForbiddenError()

    pass

private = JSONApplication('private', models=[Fruit, Basket], auth_func=basic_auth)
