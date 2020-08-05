from flask_caching import Cache
from flask_cors import CORS
from flask_mail import Mail
from flask_session import Session


session = Session()         # 会话
mail = Mail()
cors = CORS()               # 跨域请求
cache = Cache()             # 缓存

config = {
    'CACHE_TYPE': 'redis',
    'CACHE_REDIS_HOST': '127.0.0.1',
    'CACHE_REDIS_PORT': 6379
}
# # 配置日志信息，设置日志记录等级
# logging.basicConfig(level=logging.INFO)
# file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024*1024*100)  # 创建日志记录器，知名日志保存路径、以及文件的大小和文件个数上限
# formatter = logging.Formatter('%(levelname)s % (filename)s:%(lineno)d %(message)s')   # 创建日志记录格式
# file_log_handler.setFormatter(formatter)        # 设置记录格式
# logging.getLogger().addHandler(file_log_handler)        # 给flask的APP添加全局的日志记录器


def init_ext(app):

    session.init_app(app)
    mail.init_app(app)
    cors.init_app(app)
    cache.init_app(app, config=config)