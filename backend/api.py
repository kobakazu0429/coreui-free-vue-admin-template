# -*- coding: utf-8 -*-
from flask import Flask, jsonify, make_response, request
from flask_cors import CORS
from orator import DatabaseManager
import settings


db = DatabaseManager(settings.DB_CONFIG)

api = Flask(__name__)
CORS(api)


# 404の時は以下を返す
@api.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


# 全件取得
@api.route('/', methods=['GET'])
def get_tasks():
    data = []

    obj = db.table('tasks').get()

    for task in obj:
        data.append(task)

    return make_response(jsonify(data))


if __name__ == '__main__':
    api.run(host='0.0.0.0', port=settings.FLASK_PORT)
