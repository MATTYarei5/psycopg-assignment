from db import get_db


def create_company(data):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO Companies (company_name) VALUES (%s)", (data['company_name'],))
    conn.commit()
    cur.close()
    return {'status': 'success'}


def get_companies():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Companies")
    companies = cur.fetchall()
    cur.close()
    return companies


def update_company(id, data):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("UPDATE Companies SET company_name = %s WHERE company_id = %s", (data['company_name'], id))
    conn.commit()
    cur.close()
    return {'status': 'success'}


def delete_company(data):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM Companies WHERE company_id = %s", (data['company_id'],))
    conn.commit()
    cur.close()
    return {'status': 'success'}
