import json


def get_db_uri(db_info):
    database = db_info.get("DATABASE")
    driver = db_info.get("DRIVER")
    user = db_info.get("USER")
    password = db_info.get("PASSWORD")
    host = db_info.get("HOST")
    port = db_info.get("PORT")
    name = db_info.get("NAME")

    return "{}+{}://{}:{}@{}:{}/{}".format(database, driver, user, password, host, port, name)


class BaseConfig:
    JWT_SECRET_KEY = "GLLLtndksjkbvfdjkb"
    DEBUG = False
    TESTING = False
    SECRET_KEY = "vhjbknlm;'lkjkbhj423rwfsdiohn"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopConfig(BaseConfig):

    DEBUG = True

    db_info = {
        "DATABASE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "GL@LT",
        "HOST": "121.43.43.59",
        "PORT": "3306",
        "NAME": "Blog"
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(db_info)

    cache_config = {
        "CACHE_TYPE": "redis",
        "CACHE_REDIS_URL": "redis://:GLALT@121.43.43.59:6379/5"
    }

    CACHE_CONFIG = json.dumps(cache_config)


class TestingConfig(BaseConfig):

    TESTING = True

    db_info = {
        "DATABASE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "GL@LT",
        "HOST": "121.43.43.59",
        "PORT": "3306",
        "NAME": "Blog"
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(db_info)


class StagingConfig(BaseConfig):

    db_info = {
        "DATABASE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "GL@LT",
        "HOST": "121.43.43.59",
        "PORT": "3306",
        "NAME": "Blog"
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(db_info)


class OnLineConfig(BaseConfig):

    db_info = {
        "DATABASE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "GL@LT",
        "HOST": "121.43.43.59",
        "PORT": "3306",
        "NAME": "Blog"
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(db_info)


envs = {
    "develop": DevelopConfig,
    "testing": TestingConfig,
    "staging": StagingConfig,
    "online": OnLineConfig,
    "default": DevelopConfig,
}