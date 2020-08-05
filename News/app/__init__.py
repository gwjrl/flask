from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app import setting
from app.apis.new import news_bp
from app.apis.user import user_bp
from app.ext import init_ext

db = SQLAlchemy()           # 数据库关系映射


def create_app(env):

    app = Flask(__name__, static_folder="../static")

    # 获取开发环境
    config_class = setting.config_map.get(env)
    app.config.from_object(config_class)

    db.init_app(app)

    init_ext(app)
    # 注册蓝图
    app.register_blueprint(user_bp)
    app.register_blueprint(news_bp)

    return app