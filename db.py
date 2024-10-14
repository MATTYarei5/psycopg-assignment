import psycopg2


def get_db():
    conn = psycopg2.connect(
        database="your_database",
        user="your_username",
        password="your_password",
        host="localhost"
    )
    return conn


def create_tables():
    commands = (
        """
        CREATE TABLE IF NOT EXISTS Companies(
            company_id SERIAL PRIMARY KEY,
            company_name VARCHAR UNIQUE NOT NULL
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS Categories(
            category_id SERIAL PRIMARY KEY,
            category_name VARCHAR UNIQUE NOT NULL
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS Products(
            product_id SERIAL PRIMARY KEY,
            company_id INTEGER NOT NULL,
            product_name VARCHAR(255) NOT NULL,
            price DECIMAL NOT NULL,
            description TEXT,
            active BOOLEAN,
            FOREIGN KEY (company_id)
            REFERENCES Companies (company_id)
            ON UPDATE CASCADE ON DELETE CASCADE
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS Warranties(
            warranty_id SERIAL PRIMARY KEY,
            product_id INTEGER NOT NULL,
            warranty_months INTEGER NOT NULL,
            FOREIGN KEY (product_id)
            REFERENCES Products (product_id)
            ON UPDATE CASCADE ON DELETE CASCADE
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS ProductsCategoriesXref(
            product_id INTEGER NOT NULL,
            category_id INTEGER NOT NULL,
            FOREIGN KEY (product_id)
            REFERENCES Products (product_id)
            ON UPDATE CASCADE ON DELETE CASCADE,
            FOREIGN KEY (category_id)
            REFERENCES Categories (category_id)
            ON UPDATE CASCADE ON DELETE CASCADE
        )
        """
    )
    conn = None
    try:
        conn = get_db()
        cur = conn.cursor()
        for command in commands:
            cur.execute(command)
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    create_tables()
