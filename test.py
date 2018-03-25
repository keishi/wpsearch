import sys

all_ok = True

try:
    import natto
    mecab = natto.MeCab()
    mecab.parse("お元気でお過ごしですか")
    print("natto-py OK")
except ModuleNotFoundError:
    print("natto-py not found")
    all_ok = False
except :
    print("Unexpected error:", sys.exc_info()[0])
    all_ok = False

try:
    import sqlite3
    db = sqlite3.connect(':memory:')
    cursor = db.cursor()
    cursor.execute('CREATE TABLE foo(id INTEGER PRIMARY KEY, name TEXT)')
    db.commit()
    db.close()
    print("sqlite3 OK")
except ModuleNotFoundError:
    print("sqlite3 not found")
    all_ok = False
except :
    print("Unexpected error:", sys.exc_info()[0])
    all_ok = False

if all_ok:
    print("OK")
else:
    print("Failed")

sys.exit(0 if all_ok else 1)
