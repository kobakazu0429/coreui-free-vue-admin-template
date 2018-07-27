# -*- coding: utf-8 -*-
from flask import jsonify

from backend.models.Type import *
from backend.models.Group import *
from backend.models.Category import *
from backend.models.Format import *
from backend.models.Attribute import *
from backend.models.Layer import *
from backend.flask.utils.msgs import returnResultCreate, returnResultPatch, returnResultDelete


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

    for x in query:
        data.append(x)

    return jsonify(data)


def post_layer(request):
    Layer.create(
        type_id=request.form['type_id'],
        group_id=request.form['group_id'],
        category_id=request.form['category_id'],
        name=request.form['name'],
        url=request.form['url'],
        format_id=request.form['format_id'],
        attribute_id=request.form['attribute_id'],
        description=request.form['description'],
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )

    return returnResultCreate()


def patch_layer(layer_id, request):
    patching_layer = Layer.get_by_id(layer_id)

    patching_layer.type_id = request.form['type_id']
    patching_layer.group_id = request.form['group_id']
    patching_layer.category_id = request.form['category_id']
    patching_layer.name = request.form['name']
    patching_layer.url = request.form['url']
    patching_layer.format_id = request.form['format_id']
    patching_layer.attribute_id = request.form['attribute_id']
    patching_layer.description = request.form['description']
    patching_layer.updated_at = datetime.datetime.now()

    patching_layer.save()

    return returnResultPatch()


def delete_layer(layer_id):
    deleting_layer = Layer.get_by_id(layer_id)

    deleting_layer.delete_instance()

    return returnResultDelete()
