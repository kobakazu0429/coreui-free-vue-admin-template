# -*- coding: utf-8 -*-
import datetime

from backend.models.Attribute import *
from backend.flask.utils.msgs import returnResultCreate


def post_attribute(request):
    Attribute.create(
        title=request.json['title'],
        url=request.json['url'],
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now(),
    )

    return returnResultCreate()
