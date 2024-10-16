import psycopg2


def get_db_cursor(conn):
    return conn.cursor()


def create_tables():
    conn = psycopg2.connect(database="psycopg", user="mattnebeker", host="127.0.0.1", port="5432")
    cursor = get_db_cursor(conn)
    tables = [
        """
        CREATE TABLE Companies (
            company_id SERIAL PRIMARY KEY,
            company_name VARCHAR(255) NOT NULL
        )
        """,
        """
        CREATE TABLE Categories (
            category_id SERIAL PRIMARY KEY,
            category_name VARCHAR UNIQUE NOT NULL
        )
        """,
        """
        CREATE TABLE Products (
            product_id SERIAL PRIMARY KEY,
            company_id INTEGER NOT NULL,
            product_name VARCHAR(255) NOT NULL,
            price DECIMAL NOT NULL,
            description TEXT,
            active BOOLEAN NOT NULL,
            FOREIGN KEY (company_id)
            REFERENCES Companies (company_id)
            ON UPDATE CASCADE ON DELETE CASCADE
        )
        """,
        """
        CREATE TABLE ProductsCategoriesXref (
            product_id INTEGER REFERENCES Products(product_id) ON DELETE CASCADE,
            category_id INTEGER REFERENCES Categories(category_id) ON DELETE CASCADE,
            PRIMARY KEY (product_id, category_id)
        )
        """,
        """
        CREATE TABLE Warranties (
            warranty_id SERIAL PRIMARY KEY,
            product_id INTEGER NOT NULL,
            warranty_months INTEGER NOT NULL,
            FOREIGN KEY (product_id)
            REFERENCES Products (product_id)
            ON UPDATE CASCADE ON DELETE CASCADE
        )
        """
    ]
    conn = None
    try:
        conn = psycopg2.connect(database="psycopg", user="mattnebeker", host="127.0.0.1", port="5432")
        cur = conn.cursor()
        for table in tables:
            cur.execute(table)
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
