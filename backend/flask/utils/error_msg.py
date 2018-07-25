# -*- coding: utf-8 -*-
from flask import Flask, jsonify, make_response


def returnError404():
    return make_response(jsonify({'error': 'Not found'}), 404)


def returnErrorTable(table):
    return make_response(jsonify({'error': 'not exist this table [%s]' % table}), 404)
