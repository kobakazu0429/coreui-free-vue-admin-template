# -*- coding: utf-8 -*-
from flask import jsonify

from backend.models.Type import *
from backend.models.Group import *
from backend.models.Category import *
from backend.models.Format import *
from backend.models.Attribute import *


def retuenType():
    data = []
    for x in Type.select().dicts().order_by(Type.id.asc()):
        data.append(x)
    return jsonify(data)


def retuenGroup():
    data = []
    for x in Group.select().dicts().order_by(Group.id.asc()):
        data.append(x)
    return jsonify(data)


def retuenCategory():
    data = []
    for x in Category.select().dicts().order_by(Category.id.asc()):
        data.append(x)
    return jsonify(data)


def retuenFormat():
    data = []
    for x in Format.select().dicts().order_by(Format.id.asc()):
        data.append(x)
    return jsonify(data)


def retuenAttribute():
    data = []
    for x in Attribute.select().dicts().order_by(Attribute.id.asc()):
        data.append(x)
    return jsonify(data)
