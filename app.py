from clients import db
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/get-all', methods=['GET'])
def get_all():
    data = db.DatabaseClient().get_all()
    return jsonify(data)


@app.route('/query', methods=['GET'])
def get_by_query():
    data = db.DatabaseClient().get_by_query(request.args)
    return jsonify(data=data)


if __name__ == '__main__':
    app.run(debug=True)