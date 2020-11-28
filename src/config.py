import os


class BaseConfig(object):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{password}@{host}/{db_name}'.format(**{
        # 'user': "watanabetaichi",
        # 'password': "password",
        # 'host': "localhost",
        # 'db_name': "remote_ai"
        'user': os.environ.get("DATABASE_USER"),
        'password': os.environ.get("DATABASE_PASSWORD"),
        'host': os.environ.get("DATABASE_HOST"),
        'db_name': os.environ.get("DATABASE_NAME"),
    })
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
