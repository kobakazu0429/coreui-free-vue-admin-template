# -*- coding: utf-8 -*-
from flask import jsonify

from backend.models.Group import *


def get_groups():
    data = []

    for x in Group.select().order_by(Group.id).dicts():
        data.append(x)

    return jsonify(data)
