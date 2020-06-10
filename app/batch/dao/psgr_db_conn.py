# encoding utf-8
import psycopg2

class Connection:
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

    

""" sample
conn = psycopg2.connect(database = "mydb", user="training", password="training", host="localhost", port="5432")
cur = conn.cursor()

# execute sql
cur.execute("select version()")
for row in cur:
    print(row)

cur.close()
conn.close()

    - *dbname*: the database name
    - *database*: the database name (only as keyword argument)
    - *user*: user name used to authenticate
    - *password*: password used to authenticate
    - *host*: database host address (defaults to UNIX socket if not provided)
    - *port*: connection port number (defaults to 5432 if not provided)
"""
