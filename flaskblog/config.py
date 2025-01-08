import os


class Config:
    SECRET_KEY = '5791628bb0b13ce0c676dfde280ba245'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS= True
    MAIL_USE_SSL = False
    MAIL_USERNAME = 'ayushdayal8@gmail.com'
    MAIL_PASSWORD = '123'
    MAIL_DEFAULT_SENDER = 'ayushdayal8@gmail.com'