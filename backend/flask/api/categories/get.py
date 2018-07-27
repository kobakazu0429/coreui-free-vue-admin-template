# -*- coding: utf-8 -*-
from flask import jsonify

from backend.models.Category import *


def get_categories():
    data = []

    for x in Category.select().order_by(Category.id).dicts():
        data.append(x)

    return jsonify(data)
