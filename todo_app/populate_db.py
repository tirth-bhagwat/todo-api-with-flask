import os
import sys

# set path to app root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import api
from api import db
from api.models import User

with api.app.app_context():
    db.drop_all()
    db.create_all()

    # create a user
    user = User(username="admin", password="admin")
    db.session.add(user)
    db.session.commit()
