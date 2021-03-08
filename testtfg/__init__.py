import mariadb
import sys

try:
    conn = mariadb.connect(
        user = "root",
        password = "eusebiotfg",
        host = "localhost",
        port = 3306,
    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB: {e}")
    sys.exit(1)

cur = conn.cursor()
cur.execute(
    "USE test"
)
cur.execute(
    "SELECT * FROM myTable"
)

for (col1, col2) in cur:
    print(f"Col1: {col1}, Col2: {col2}")