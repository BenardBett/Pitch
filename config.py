import os

class Config:

    MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'
    MOVIE_API_KEY = os.environ.get('MOVIE_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/pitch'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    
# simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
#  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")



class ProdConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://james:password@localhost/watchlist_test'

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI="postgres://moringa:Access@localhost/pitch"
    DEVELOPMENT = True
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}