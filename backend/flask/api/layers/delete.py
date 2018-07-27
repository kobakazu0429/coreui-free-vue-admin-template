# -*- coding: utf-8 -*-
from backend.models.Layer import *

from backend.flask.utils.msgs import returnResultDelete


def delete_layer(layer_id):
    deleting_layer = Layer.get_by_id(layer_id)

    deleting_layer.delete_instance()

    return returnResultDelete()
