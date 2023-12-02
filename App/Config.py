class Config:
    #SECRET_KEY = 'B!1w8NAt1T^%kvhUI*S^'
    SECRET_KEY = 'MPNG'

class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
    MYSQL_DB = 'Ticket_Turno'


config = {
    'development': DevelopmentConfig
}