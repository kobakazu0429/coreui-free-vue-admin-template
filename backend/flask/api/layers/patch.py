# -*- coding: utf-8 -*-
from backend.models.Layer import *

from backend.flask.utils.msgs import returnResultPatch


def patch_layer(layer_id, request):
    patching_layer = Layer.get_by_id(layer_id)

    patching_layer.type_id = request.json['type_id']
    patching_layer.group_id = request.json['group_id']
    patching_layer.category_id = request.json['category_id']
    patching_layer.name = request.json['name']
    patching_layer.url = request.json['url']
    patching_layer.format_id = request.json['format_id']
    patching_layer.attribute_id = request.json['attribute_id']
    patching_layer.description = request.json['description']
    patching_layer.is_active = request.json['is_active']
    patching_layer.updated_at = datetime.datetime.now()

    patching_layer.save()

    return returnResultPatch()
