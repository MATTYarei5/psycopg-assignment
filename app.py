from flask import Flask, request, jsonify
from db import get_db_cursor, create_tables
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(database="psycopg", user="mattnebeker", host="127.0.0.1", port="5432")


@app.route('/company', methods=['POST'])
def create_company():
    company_name = request.json['company_name']
    cursor = get_db_cursor(conn)
    cursor.execute("INSERT INTO Companies (company_name) VALUES (%s)", (company_name,))
    conn.commit()
    cursor.execute("SELECT * FROM Companies WHERE company_name = %s", (company_name,))
    result = cursor.fetchone()
    if result:
        company_list = []
        company_record = {
            'company_id': result[0],
            'company_name': result[1]
        }
        company_list.append(company_record)

    return jsonify({"message": "company created", "results": company_list}), 201


@app.route('/company/<int:company_id>', methods=['GET'])
def read_company(company_id):
    cursor = get_db_cursor(conn)
    cursor.execute("SELECT * FROM Companies WHERE company_id = %s", (company_id,))
    company = cursor.fetchone()
    if company:
        company_record = {
            'company_id': company[0],
            'company_name': company[1]
        }
        return jsonify(company_record), 200
    return jsonify({"message": "company not found"}), 404


@app.route('/companies', methods=['GET'])
def read_all_companies():
    cursor = get_db_cursor(conn)
    cursor.execute("SELECT * FROM Companies")
    results = cursor.fetchall()
    companies = []
    for result in results:
        company_record = {
            'company_id': result[0],
            'company_name': result[1]
        }
        companies.append(company_record)
    return jsonify(companies), 200


@app.route('/company/<int:company_id>', methods=['PUT'])
def update_company(company_id):
    company_name = request.json['company_name']
    cursor = get_db_cursor(conn)
    cursor.execute("UPDATE Companies SET company_name = %s WHERE company_id = %s", (company_name, company_id))
    conn.commit()
    cursor.execute("SELECT * FROM Companies WHERE company_name = %s", (company_name,))
    result = cursor.fetchone()
    if result:
        company_list = []
        company_record = {
            'company_id': result[0],
            'company_name': result[1]
        }
        company_list.append(company_record)
        return jsonify({"message": "company updated", "results": company_list}), 200
    return jsonify({"message": "company not found"}), 404


@app.route('/company/<int:company_id>', methods=['DELETE'])
def delete_company(company_id):
    cursor = get_db_cursor(conn)
    cursor.execute("DELETE FROM Companies WHERE company_id = %s", (company_id,))
    return jsonify({"message": "company deleted"}), 200


@app.route('/category', methods=['POST'])
def create_category():
    category_name = request.json['category_name']
    cursor = get_db_cursor(conn)
    cursor.execute("INSERT INTO Categories (category_name) VALUES (%s)", (category_name,))
    conn.commit()
    cursor.execute("SELECT * FROM Categories WHERE category_name = %s", (category_name,))
    result = cursor.fetchone()
    if result:
        category_list = []
        category_record = {
            'category_id': result[0],
            'category_name': result[1]
        }
        category_list.append(category_record)
    return jsonify({"message": "category created", "results": category_list}), 201


@app.route('/category/<int:category_id>', methods=['GET'])
def read_category(category_id):
    cursor = get_db_cursor(conn)
    cursor.execute("SELECT * FROM Categories WHERE category_id = %s", (category_id,))
    result = cursor.fetchone()
    if result:
        category_list = []
        category_record = {
            'category_id': result[0],
            'category_name': result[1]
        }
        category_list.append(category_record)
        return jsonify({"message": "category fetched", "results": category_list}), 200
    return jsonify({"message": "category not found"}), 404


@app.route('/categories', methods=['GET'])
def read_all_categories():
    cursor = get_db_cursor(conn)
    cursor.execute("SELECT * FROM Categories")
    results = cursor.fetchall()
    categories = []
    for result in results:
        category_record = {
            'category_id': result[0],
            'category_name': result[1]
        }
        categories.append(category_record)
    return jsonify({"message": "categories fetched", "results": categories}), 200


@app.route('/category/<int:category_id>', methods=['PUT'])
def update_category(category_id):
    category_name = request.json['category_name']
    cursor = get_db_cursor(conn)
    cursor.execute("UPDATE Categories SET category_name = %s WHERE category_id = %s", (category_name, category_id))
    conn.commit()
    cursor.execute("SELECT * FROM Categories WHERE category_name = %s", (category_name,))
    result = cursor.fetchone()
    if result:
        category_list = []
        category_record = {
            'category_id': result[0],
            'category_name': result[1]
        }
        category_list.append(category_record)
        return jsonify({"message": "category updated", "results": category_list}), 200
    return jsonify({"message": "category not found"}), 404


@app.route('/category/<int:category_id>', methods=['DELETE'])
def delete_category(category_id):
    cursor = get_db_cursor(conn)
    cursor.execute("DELETE FROM Categories WHERE category_id = %s", (category_id,))
    return jsonify({"message": "category deleted"}), 200


@app.route('/product', methods=['POST'])
def create_product():
    company_id = request.json['company_id']
    product_name = request.json['product_name']
    price = request.json['price']
    description = request.json['description']
    active = request.json['active']
    cursor = get_db_cursor(conn)
    cursor.execute("INSERT INTO Products (company_id, product_name, price, description, active) VALUES (%s, %s, %s, %s, %s)", (company_id, product_name, price, description, active,))
    conn.commit()
    cursor.execute("SELECT * FROM Products WHERE company_id = %s AND product_name = %s AND price = %s AND description = %s AND active = %s", (company_id, product_name, price, description, active,))
    result = cursor.fetchone()
    if result:
        product_list = []
        product_record = {
            'product_id': result[0],
            'company_id': result[1],
            'product_name': result[2],
            'price': result[3],
            'description': result[4],
            'active': result[5]
        }
        product_list.append(product_record)
    return jsonify({"message": "product created", "results": product_list}), 201


@app.route('/product/<int:product_id>', methods=['GET'])
def read_product(product_id):
    cursor = get_db_cursor(conn)
    cursor.execute("SELECT * FROM Products WHERE product_id = %s", (product_id,))
    result = cursor.fetchone()
    if result:
        product_list = []
        product_record = {
            'product_id': result[0],
            'company_id': result[1],
            'product_name': result[2],
            'price': result[3],
            'description': result[4],
            'active': result[5]
        }
        product_list.append(product_record)
        return jsonify({"message": "product fetched", "results": product_list}), 200
    return jsonify({"message": "product not found"}), 404


@app.route('/products', methods=['GET'])
def read_all_products():
    cursor = get_db_cursor(conn)
    cursor.execute("SELECT * FROM Products")
    results = cursor.fetchall()
    products = []
    for result in results:
        product_record = {
            'product_id': result[0],
            'company_id': result[1],
            'product_name': result[2],
            'price': result[3],
            'description': result[4],
            'active': result[5]
        }
        products.append(product_record)
    return jsonify({"message": "products fetched", "results": products}), 200


@app.route('/product/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    company_id = request.json['company_id']
    product_name = request.json['product_name']
    price = request.json['price']
    description = request.json['description']
    active = request.json['active']
    cursor = get_db_cursor(conn)
    cursor.execute("UPDATE Products SET company_id = %s, product_name = %s, price = %s, description = %s, active = %s WHERE product_id = %s", (company_id, product_name, price, description, active, product_id))
    conn.commit()
    cursor.execute("SELECT * FROM Products WHERE product_id = %s", (product_id,))
    result = cursor.fetchone()
    if result:
        product_list = []
        product_record = {
            'product_id': result[0],
            'company_id': result[1],
            'product_name': result[2],
            'price': result[3],
            'description': result[4],
            'active': result[5]
        }
        product_list.append(product_record)
        return jsonify({"message": "product updated", "results": product_list}), 200
    return jsonify({"message": "product not found"}), 404


@app.route('/product/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    cursor = get_db_cursor(conn)
    cursor.execute("DELETE FROM Products WHERE product_id = %s", (product_id,))
    return jsonify({"message": "product deleted"}), 200


@app.route('/warranty', methods=['POST'])
def create_warranty():
    product_id = request.json['product_id']
    warranty_months = request.json['warranty_months']
    cursor = get_db_cursor(conn)
    cursor.execute("INSERT INTO Warranties (product_id, warranty_months) VALUES (%s, %s)", (product_id, warranty_months,))
    conn.commit()
    cursor.execute("SELECT * FROM Warranties WHERE product_id = %s AND warranty_months = %s", (product_id, warranty_months,))
    result = cursor.fetchone()
    if result:
        warranty_list = []
        warranty_record = {
            'warranty_id': result[0],
            'product_id': result[1],
            'warranty_months': result[2]
        }
        warranty_list.append(warranty_record)
    return jsonify({"message": "warranty created", "results": warranty_list}), 201


@app.route('/warranty/<int:warranty_id>', methods=['GET'])
def read_warranty(warranty_id):
    cursor = get_db_cursor(conn)
    cursor.execute("SELECT * FROM Warranties WHERE warranty_id = %s", (warranty_id,))
    result = cursor.fetchone()
    if result:
        warranty_list = []
        warranty_record = {
            'warranty_id': result[0],
            'product_id': result[1],
            'warranty_months': result[2]
        }
        warranty_list.append(warranty_record)
        return jsonify({"message": "warranty fetched", "results": warranty_list}), 200
    return jsonify({"message": "warranty not found"}), 404


@app.route('/warranties', methods=['GET'])
def read_all_warranties():
    cursor = get_db_cursor(conn)
    cursor.execute("SELECT * FROM Warranties")
    results = cursor.fetchall()
    warranties = []
    for result in results:
        warranty_record = {
            'warranty_id': result[0],
            'product_id': result[1],
            'warranty_months': result[2]
        }
        warranties.append(warranty_record)
    return jsonify({"message": "warranties fetched", "results": warranties}), 200


@app.route('/warranty/<int:warranty_id>', methods=['PUT'])
def update_warranty(warranty_id):
    product_id = request.json['product_id']
    warranty_months = request.json['warranty_months']
    cursor = get_db_cursor(conn)
    cursor.execute("UPDATE Warranties SET product_id = %s, warranty_months = %s WHERE warranty_id = %s", (product_id, warranty_months, warranty_id))
    conn.commit()
    cursor.execute("SELECT * FROM Warranties WHERE warranty_id = %s", (warranty_id,))
    result = cursor.fetchone()
    if result:
        warranty_list = []
        warranty_record = {
            'warranty_id': result[0],
            'product_id': result[1],
            'warranty_months': result[2]
        }
        warranty_list.append(warranty_record)
        return jsonify({"message": "warranty updated", "results": warranty_list}), 200
    return jsonify({"message": "warranty not found"}), 404


@app.route('/warranty/<int:warranty_id>', methods=['DELETE'])
def delete_warranty(warranty_id):
    cursor = get_db_cursor(conn)
    cursor.execute("DELETE FROM Warranties WHERE warranty_id = %s", (warranty_id,))
    return jsonify({"message": "warranty deleted"}), 200


@app.route('/productscategory', methods=['POST'])
def create_product_category():
    product_id = request.json['product_id']
    category_id = request.json['category_id']
    cursor = get_db_cursor(conn)
    cursor.execute("INSERT INTO ProductsCategoriesXref (product_id, category_id) VALUES (%s, %s)", (product_id, category_id,))
    conn.commit()
    cursor.execute("SELECT * FROM ProductsCategoriesXref WHERE product_id = %s AND category_id = %s", (product_id, category_id,))
    result = cursor.fetchone()
    if result:
        product_category_list = []
        product_category_record = {
            'xref_id': result[0],
            'product_id': result[1],
            'category_id': result[2]
        }
        product_category_list.append(product_category_record)
    return jsonify({"message": "product category created", "results": product_category_list}), 201


@app.route('/productscategory/<int:xref_id>', methods=['GET'])
def read_product_category(xref_id):
    cursor = get_db_cursor(conn)
    cursor.execute("SELECT * FROM ProductsCategoriesXref WHERE xref_id = %s", (xref_id,))
    result = cursor.fetchone()
    if result:
        product_category_list = []
        product_category_record = {
            'xref_id': result[0],
            'product_id': result[1],
            'category_id': result[2]
        }
        product_category_list.append(product_category_record)
        return jsonify({"message": "product category fetched", "results": product_category_list}), 200
    return jsonify({"message": "product category not found"}), 404


@app.route('/productscategory', methods=['GET'])
def read_all_product_categories():
    cursor = get_db_cursor(conn)
    cursor.execute("SELECT * FROM ProductsCategoriesXref")
    results = cursor.fetchall()
    product_categories = []
    for result in results:
        product_category_record = {
            'xref_id': result[0],
            'product_id': result[1],
            'category_id': result[2]
        }
        product_categories.append(product_category_record)
    return jsonify({"message": "product categories fetched", "results": product_categories}), 200


@app.route('/productscategory/<int:xref_id>', methods=['PUT'])
def update_product_category(xref_id):
    product_id = request.json['product_id']
    category_id = request.json['category_id']
    cursor = get_db_cursor(conn)
    cursor.execute("UPDATE ProductsCategoriesXref SET product_id = %s, category_id = %s WHERE xref_id = %s", (product_id, category_id, xref_id))
    conn.commit()
    cursor.execute("SELECT * FROM ProductsCategoriesXref WHERE xref_id = %s", (xref_id,))
    result = cursor.fetchone()
    if result:
        product_category_list = []
        product_category_record = {
            'xref_id': result[0],
            'product_id': result[1],
            'category_id': result[2]
        }
        product_category_list.append(product_category_record)
        return jsonify({"message": "product category updated", "results": product_category_list}), 200
    return jsonify({"message": "product category not found"}), 404


@app.route('/productscategory/<int:xref_id>', methods=['DELETE'])
def delete_product_category(xref_id):
    cursor = get_db_cursor(conn)
    cursor.execute("DELETE FROM ProductsCategoriesXref WHERE xref_id = %s", (xref_id,))
    return jsonify({"message": "product category deleted"}), 200


if __name__ == "__main__":
    create_tables()
    app.run(host='0.0.0.0', port='8086')
