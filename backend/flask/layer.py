# -*- coding: utf-8 -*-
from flask import jsonify

from backend.models.Type import *
from backend.models.Group import *
from backend.models.Category import *
from backend.models.Format import *
from backend.models.Attribute import *
from backend.models.Layer import *


def get_layer(layer_id):
    data = []

    where_cond = None

    if layer_id is not None:
        where_cond = (Layer.id == layer_id)

    query = (Layer
             .select(
                 Layer.id,
                 Layer.name,
                 Layer.url,
                 Layer.description,
                 Type.type,
                 Group.group,
                 Category.category,
                 Format.format,
                 Attribute.title.alias('attribute_title'),
                 Attribute.url.alias('attribute_utl')
             )
             .join(Type, on=(Layer.type_id == Type.id))
             .join(Group, on=(Layer.group_id == Group.id))
             .join(Category, on=(Layer.category_id == Category.id))
             .join(Format, on=(Layer.format_id == Format.id))
             .join(Attribute, on=(Layer.attribute_id == Attribute.id))
             .where(where_cond)
             .order_by(Layer.id)
             .dicts())


# for x in Layer.select().order_by(Layer.id).dicts():
    for x in query:
        data.append(x)

    return jsonify(data)
