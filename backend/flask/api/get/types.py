# -*- coding: utf-8 -*-
from flask import jsonify

from backend.models.Type import *


def get_types():
    data = []

    for x in Type.select().order_by(Type.id).dicts():
        data.append(x)

    return jsonify(data)
