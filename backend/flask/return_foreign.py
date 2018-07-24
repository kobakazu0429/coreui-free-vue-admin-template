# -*- coding: utf-8 -*-
from flask import jsonify

from backend.models.Type import *
from backend.models.Group import *
from backend.models.Category import *
from backend.models.Format import *
from backend.models.Attribute import *


def returnForeign(foreign):
    if (foreign == 'types'):
        this_class = Type()
    elif (foreign == 'groups'):
        this_class = Group()
    elif (foreign == 'categories'):
        this_class = Category()
    elif (foreign == 'formats'):
        this_class = Format()
    elif (foreign == 'attributes'):
        this_class = Attribute()
    else:
        return

    data = []

    for x in this_class.select().order_by(this_class.id).dicts():
        data.append(x)

    return jsonify(data)
