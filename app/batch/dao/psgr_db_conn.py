# encoding utf-8
import psycopg2
import conf.onithon_config as conf


# TODO:シングルトン実装 
# loggingクラスがドキュメント読む限りシングルトン実装？ https://github.com/python/cpython/blob/3.8/Lib/logging/__init__.py
class Connection:
    """
    コネクション情報を保持する
    インスタンスメソッドはPEP249準拠
    """
    def __init__(self):
        config = conf.OnithonConfig()
        db = config.getvalue('DB_CONN_INFO', 'ONITHON_DB')
        usr = config.getvalue('DB_CONN_INFO', 'ONITHON_DB_USER')
        pw = config.getvalue('DB_CONN_INFO', 'ONITHON_DB_PW')
        hst = config.getvalue('DB_CONN_INFO', 'ONITHON_DB_HST')
        prt = config.getvalue('DB_CONN_INFO', 'ONITHON_DB_PORT')
        self.conn = psycopg2.connect(database = db, user = usr, password = pw, host = hst, port = prt)
    
    def close(self):
        self.conn.close()

    def commit(self):
        self.conn.commit()

    def rollback(self):
        self.conn.rollback

    def cursor(self):
        return self.conn.cursor()
