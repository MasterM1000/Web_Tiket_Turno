from flask_mysqldb import MySQL
class Singleton(object):

    def __init__(self, app):
        super().__init__()
        self.mysql = MySQL(app)
        self.app = app

    @staticmethod
    def getInstance(app):
        if not hasattr(Singleton, "_instance"):
            Singleton._instance = Singleton(app)
        return Singleton._instance

