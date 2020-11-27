import os


class BaseConfig(object):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{password}@{host}/{db_name}'.format(**{
        'user': "watanabetaichi",
        'password': "password",
        'host': "localhost",
        'db_name': "remote_ai"
    })
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
