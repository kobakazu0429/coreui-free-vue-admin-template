# -*- coding: utf-8 -*-
from backend.models.Layer import *

from backend.flask.utils.msgs import returnResultCreate


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
