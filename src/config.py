class DevelopmentConfig:
    DEBUG = True


class Config:
    SECRET_KEY = "djqifhuqebq12dDeheh*sS23"


class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = "localhost"
    MYSQL_USER = "root"
    MYSQL_PASSWORD = ""
    MYSQL_DB = "flask_login"


config = {"development": DevelopmentConfig}
