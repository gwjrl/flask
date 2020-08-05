import os


def get_database(db_info):
    database = db_info.get("DATABASE")
    driver = db_info.get("DRIVER")
    user = db_info.get("USER")
    password = db_info.get("PASSWORD")
    host = db_info.get("HOST")
    port = db_info.get("PORT")
    name = db_info.get("NAME")

    return "{}+{}://{}:{}@{}:{}/{}".format(database, driver, user, password, host, port, name)


class BaseConfig:
    '''配置信息'''
    DEBUG = True
    SECRET_KEY = "skfhdkjcb1234KNNBJ*KLJ"

    # 数据库
    db_info = {
        "DATABASE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "123456",
        "HOST": "127.0.0.1",
        "PORT": "3306",
        "NAME": "news"
    }
    SQLALCHEMY_DATABASE_URI = get_database(db_info)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_TEARDOWN = True

    # 项目路径
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    STATIC_DIR = os.path.join(BASE_DIR, 'static')
    TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
    # 头像上传路径
    UPLOAD_ICON_DIR = os.path.join(STATIC_DIR, 'upload/icon')


    # 邮箱
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_PORT = 465  # 如果启用ssl其值是465，如果不启用 请用25
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'xxxxxx'  # 邮箱账号
    MAIL_PASSWORD = 'xxxxxxx'  # stmp密码
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = 'xxx@qq.com'  # 邮箱地址
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')

    # # redis
    # REDIS_HOST = "redis host"
    # REDIS_PORT = 6379

    # flask-session 配置
    # SESSION_TYPE = "redis"
    # SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    # SESSION_USE_SIGNER = True                      # 对cookie中的session_id 进行隐藏处理
    # PERMANENT_SESSION_LIFETIME = 86400


class DevelopmentConfig(BaseConfig):
    '''开发环境配置'''
    DEBUG = True


class ProductionConfig(BaseConfig):
    '''生产环境配置'''
    DEBUG = False


config_map = {
    "develop": DevelopmentConfig,
    "product": ProductionConfig
}