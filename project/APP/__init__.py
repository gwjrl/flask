from flask import Flask

from APP.apis import init_route
from APP.config import envs
from APP.extension import init_ext
from APP.middleware import load_middleware


def create_app(env):
    app = Flask(__name__, static_folder="../static", template_folder="../templates")

    # 加载配置文件
    app.config.from_object(envs.get(env))

    # 加载第三方插件
    init_ext(app)

    init_route(app)
    # 加载钩子函数 加载中间件
    load_middleware(app)

    return app