# -*- coding: utf-8 -*-
from backend.models.Layer import *

from backend.flask.utils.msgs import returnResultCreate


def post_layer(request):
    Layer.create(
        type_id=request.json['type_id'],
        group_id=request.json['group_id'],
        category_id=request.json['category_id'],
        name=request.json['name'],
        url=request.json['url'],
        format_id=request.json['format_id'],
        attribute_id=request.json['attribute_id'],
        description=request.json['description'],
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now()
    )

    return returnResultCreate()
