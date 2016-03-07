from config_no_commit import DRCHRONO_APP_ID, DRCHRONO_APP_SECRET
import os
_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

ADMINS = frozenset(['example@example.com'])
SECRET_KEY = 'SECRET_KEY1'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'app.db')
DATABASE_CONNECT_OPTIONS = {}

WTF_CSRF_ENABLED = False
WTF_CSRF_SECRET_KEY = "SECRET_KEY2"
