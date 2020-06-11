# encoding utf-8
import psycopg2

# TODO:シングルトン実装
class Connection:
    """
    コネクション情報を保持する
    インスタンスメソッドはPEP249準拠
    """
    def __init__(self):
        db = "mydb"
        usr = "training"
        pw = "training"
        hst = "localhost"
        prt = "5432"
        self.conn = psycopg2.connect(database = db, user = usr, password = pw, host = hst, port = prt)
    
    def close(self):
        self.conn.close()

    def commit(self):
        self.conn.commit()

    def rollback(self):
        self.conn.rollback

    def cursor(self):
        return self.conn.cursor()
