import json

from flask_caching import Cache
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()
cache = Cache()


def init_ext(app):
    db.init_app(app)
    migrate.init_app(app, db)
    cache.init_app(app, config=json.loads(app.config.get("CACHE_CONFIG")))

