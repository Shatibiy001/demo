import sqlite3
import sys

db='db.sqlite3'
con=sqlite3.connect(db)
cur=con.cursor()
try:
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    print('TABLES:', cur.fetchall())
    cur.execute("SELECT count(*) FROM project_project;")
    print('COUNT:', cur.fetchone()[0])
    cur.execute("SELECT id, title, owner_id FROM project_project ORDER BY created DESC LIMIT 20;")
    rows=cur.fetchall()
    print('ROWS:')
    for r in rows:
        print(r)
except Exception as e:
    print('ERROR', e)
finally:
    con.close()
