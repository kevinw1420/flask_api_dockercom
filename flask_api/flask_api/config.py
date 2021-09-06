class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True
    DOMAIN = 'http://127.0.0.1:8000'
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:Passw0rd@db:3306/flask_api"
    SECRET_KEY = 'asdjfoasjduwrqowjfpsajdofpaspa'
    
config = {
    'default': DevelopmentConfig
}