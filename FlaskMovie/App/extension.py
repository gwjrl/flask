import json

from flask_caching import Cache
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


migrate = Migrate()
cache = Cache()
db = SQLAlchemy()

def init_ext(app):
    db.init_app(app)
    migrate.init_app(app, db)
    # 解决跨域
    CORS(app, supports_credentials=True)
    cache.init_app(app, config=json.loads(app.config.get("CACHE_CONFIG")))