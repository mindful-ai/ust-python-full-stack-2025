# Docker + PostgreSQL + Python CRUD Assessment

## Assessment Problem Statement

Your task is to:

1.  Use **Docker** to run a **PostgreSQL** database locally.
2.  Ensure the database is accessible from your host machine.
3.  Create a Python script using **psycopg2** module to perform full
    **CRUD**:
    -   Create a table
    -   Insert records
    -   Read records
    -   Update a record
    -   Delete a record
4.  Verify each operation by printing results to the console.
5.  Submit:
    -   Docker compose file: `docker-compose.yml`
    -   Python CRUD script
    -   Screenshots of CRUD output

------------------------------------------------------------------------

## Sample Docker Command

``` bash
docker run --name mypg   -e POSTGRES_USER=postgres   -e POSTGRES_PASSWORD=admin123   -e POSTGRES_DB=testdb   -p 5432:5432   -d postgres
```

------------------------------------------------------------------------

## Python CRUD Script (psycopg2)

``` python
import psycopg2

def get_conn():
    return psycopg2.connect(
        dbname="testdb",
        user="postgres",
        password="admin123",
        host="localhost",
        port=5432
    )

def create_table():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            age INT
        );
    """)
    conn.commit()
    conn.close()
    print("Table created")

def insert_student(name, age):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("INSERT INTO students (name, age) VALUES (%s, %s)", (name, age))
    conn.commit()
    conn.close()
    print("Inserted:", name)

def read_students():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    conn.close()
    print("Students:", rows)

def update_student(student_id, new_age):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("UPDATE students SET age=%s WHERE id=%s", (new_age, student_id))
    conn.commit()
    conn.close()
    print("Updated ID:", student_id)

def delete_student(student_id):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("DELETE FROM students WHERE id=%s", (student_id,))
    conn.commit()
    conn.close()
    print("Deleted ID:", student_id)

if __name__ == "__main__":
    create_table()
    insert_student("Arjun", 21)
    insert_student("Meera", 23)
    read_students()
    update_student(1, 25)
    read_students()
    delete_student(2)
    read_students()
```
