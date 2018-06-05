import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False # Signal to app before any change is made

    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USE_SSL=False
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = MAIL_USERNAME
    MAIL_MAX_EMAILS=None
    POSTS_PER_PAGE = 25
    ADMINS = ['james.e.b.rushton@gmail.com']
    """
    ADMINS = ['james.e.b.rushton@gmail.com']
    POSTS_PER_PAGE = 25
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    #MAIL_SERVER = 'smtp.gmail.com'
    #MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS=True
    MAIL_USE_SSL=False
    MAIL_USERNAME='james.e.b.rushton@gmail.com'
    MAIL_PASSWORD='Kunststoff44'
    MAIL_DEFAULT_SENDER = MAIL_USERNAME
    MAIL_MAX_EMAILS=None
    # MAIL_SUPPRESS_SEND=  app.testing
    # MAIL_ASCII_ATTACHMENTS: default
    """




