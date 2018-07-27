# -*- coding: utf-8 -*-
from flask import jsonify

from backend.models.Attribute import *


def get_attributes():
    data = []

    for x in Attribute.select().order_by(Attribute.id).dicts():
        data.append(x)

    return jsonify(data)
