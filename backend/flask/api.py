# -*- coding: utf-8 -*-
import sys
sys.path.append("..")

from flask import Flask, jsonify, make_response, request
from flask_cors import CORS

from backend.config import settings
from backend.flask.foreign import *
from backend.flask.layer import *

from backend.flask.utils.error_msg import *

api = Flask(__name__)
CORS(api)


# 404の時は以下を返す
@api.errorhandler(404)
def not_found(error):
    return returnError404()


# 処理する前にdbへ接続する
@api.before_request
def before_request_handler():
    db.connect()


# 処理した後にdbを切断する
@api.teardown_request
def after_request_handler(exc):
    if not db.is_closed():
        db.close()


# foreign
@api.route('/api/<string:foreign>', defaults={'id': None}, methods=['GET', 'POST', 'PATCH', 'DELETE'])
@api.route('/api/<string:foreign>/<int:id>', methods=['GET', 'POST', 'PATCH', 'DELETE'])
def swicth_foreign(foreign, id):
    if foreign in ['types', 'groups', 'categories', 'formats', 'attributes']:
        if request.method == 'GET':
            return make_response(get_foreign(foreign))
        elif request.method == 'POST':
            return make_response(post_foreign(foreign, request))
        elif request.method == 'PATCH':
            return make_response(patch_foreign(foreign, id, request))
        elif request.method == 'DELETE':
            return make_response(delete_foreign(foreign, id, request))
        else:
            return returnError404()

    else:
        return returnErrorTable(foreign)


# layer
@api.route('/api/layer/', defaults={'id': None}, methods=['GET', 'POST', 'PATCH', 'DELETE'])
@api.route('/api/layer/<int:id>', methods=['GET', 'POST', 'PATCH', 'DELETE'])
def returnLayerFunc(id):
    return make_response(get_layer(id))


if __name__ == '__main__':
    api.run(host='0.0.0.0', port=settings.FLASK_PORT)
