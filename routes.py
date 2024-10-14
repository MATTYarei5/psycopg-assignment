from flask import Flask, request, jsonify
from controllers import create_company, get_companies, update_company

app = Flask(__name__)


@app.route('/company', methods=['POST'])
def create_company_route():
    data = request.get_json()
    result = create_company(data)
    return jsonify(result)


@app.route('/companies', methods=['GET'])
def get_companies_route():
    companies = get_companies()
    return jsonify(companies)


@app.route('/company/<id>', methods=['PUT'])
def update_company_route(id):
    data = request.get_json()
    result = update_company(id, data)
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
