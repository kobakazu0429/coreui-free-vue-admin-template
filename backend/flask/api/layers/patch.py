# -*- coding: utf-8 -*-
from backend.models.Layer import *

from backend.flask.utils.msgs import returnResultPatch


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
