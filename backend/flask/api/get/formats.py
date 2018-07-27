# -*- coding: utf-8 -*-
from flask import jsonify

from backend.models.Format import *


def get_formats():
    data = []

    for x in Format.select().order_by(Format.id).dicts():
        data.append(x)

    return jsonify(data)
