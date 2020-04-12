from flask import Flask


from App.apis import init_api
from App.config import envs
from App.extension import init_ext
from App.middleware import load_middleware


def create_app(env):
    app = Flask(__name__, static_folder="../static", template_folder="../templates")

    # 加载配置文件
    app.config.from_object(envs.get(env))

    # 加载第三方插件
    init_ext(app)

    # 加载钩子函数 加载中间件
    load_middleware(app)

    init_api(app)

    return app