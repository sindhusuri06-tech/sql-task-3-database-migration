# SQL Internship Task 3 - Database Migration

## Objective
Migrate data from MySQL to PostgreSQL.

## Tools Used
- MySQL
- PostgreSQL
- Python
- mysql-connector
- psycopg2

## Files
- mysql_dump.sql → MySQL database export
- postgres_schema.sql → PostgreSQL table
- migrate.py → Migration script
- README.md → Documentation

## Steps

1. Import MySQL database
   mysql -u root -p < mysql_dump.sql

2. Create PostgreSQL table
   psql -U postgres -d company_db -f postgres_schema.sql

3. Run migration script
   python migrate.py

4. Verify data in PostgreSQL
   SELECT * FROM employees;

## Output
Data successfully migrated from MySQL to PostgreSQL.

## Author
Sindhu S
