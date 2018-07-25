# -*- coding: utf-8 -*-
import sys
sys.path.append("..")

from flask import Flask, jsonify, make_response
from flask_cors import CORS

from backend.config import settings
from backend.flask.get.foreigns import *

api = Flask(__name__)
CORS(api)


# 404の時は以下を返す
@api.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


# 処理する前にdbへ接続する
@api.before_request
def before_request_handler():
    db.connect()


# 処理した後にdbを切断する
@api.teardown_request
def after_request_handler(exc):
    if not db.is_closed():
        db.close()


# return foreigns
@api.route('/api/<string:foreign>', methods=['GET'])
def swictherReturn(foreign):
    if foreign in ['types', 'groups', 'categories', 'formats', 'attributes']:
        return make_response(returnForeign(foreign))
    else:
        return make_response(jsonify({'error': 'not exist this table [%s]' % foreign}), 404)


if __name__ == '__main__':
    api.run(host='0.0.0.0', port=settings.FLASK_PORT)
