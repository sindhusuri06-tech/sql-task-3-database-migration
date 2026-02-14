import mysql.connector
import psycopg2

# MySQL Connection
mysql_conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="company"
)

mysql_cursor = mysql_conn.cursor()

# PostgreSQL Connection
pg_conn = psycopg2.connect(
    host="localhost",
    database="company_db",
    user="postgres",
    password="password"
)

pg_cursor = pg_conn.cursor()

# Fetch Data from MySQL
mysql_cursor.execute("SELECT * FROM employees")
rows = mysql_cursor.fetchall()

# Insert into PostgreSQL
for row in rows:
    pg_cursor.execute(
        "INSERT INTO employees VALUES (%s, %s, %s, %s)",
        row
    )

pg_conn.commit()

print("Data Migration Completed Successfully!")

mysql_conn.close()
pg_conn.close()
